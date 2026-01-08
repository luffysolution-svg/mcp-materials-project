#!/usr/bin/env python3
"""
Materials Search CLI - Query Materials Project database
Usage: python materials_search.py [options]
"""

import os
import sys
import json
import argparse
from datetime import datetime

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

try:
    from mp_api.client import MPRester
except ImportError:
    print(json.dumps({
        "error": "mp-api not installed. Run: pip install mp-api",
        "status": "error"
    }))
    sys.exit(1)


def serialize_object(obj):
    """Convert objects to JSON-serializable format"""
    if obj is None:
        return None
    if isinstance(obj, (str, int, float, bool)):
        return obj
    if isinstance(obj, (list, tuple)):
        return [serialize_object(item) for item in obj]
    if isinstance(obj, dict):
        return {str(k): serialize_object(v) for k, v in obj.items()}
    if hasattr(obj, 'tolist'):
        return obj.tolist()
    if hasattr(obj, 'as_dict'):
        return serialize_object(obj.as_dict())
    if hasattr(obj, '__dict__'):
        return serialize_object(obj.__dict__)
    return str(obj)


def search_materials(args):
    """Search materials based on criteria"""
    api_key = os.environ.get("MP_API_KEY")
    if not api_key:
        return {
            "error": "MP_API_KEY environment variable not set",
            "status": "error"
        }

    try:
        with MPRester(api_key) as mpr:
            search_params = {
                "num_chunks": 1,
                "chunk_size": args.limit
            }

            # Build search parameters
            if args.material_id:
                search_params["material_ids"] = [args.material_id]
            if args.formula:
                search_params["formula"] = args.formula
            if args.elements:
                search_params["elements"] = args.elements.split(",")
            if args.chemsys:
                search_params["chemsys"] = args.chemsys

            # Band gap filter
            if args.band_gap_min is not None or args.band_gap_max is not None:
                bg_min = args.band_gap_min if args.band_gap_min is not None else 0
                bg_max = args.band_gap_max if args.band_gap_max is not None else 100
                search_params["band_gap"] = (bg_min, bg_max)

            # Boolean filters
            if args.stable:
                search_params["is_stable"] = True
            if args.metal:
                search_params["is_metal"] = True
            if args.magnetic:
                search_params["is_magnetic"] = True

            # Basic fields for quick results
            fields = [
                "material_id", "formula_pretty", "band_gap",
                "energy_above_hull", "is_stable", "is_metal",
                "formation_energy_per_atom", "density", "symmetry"
            ]
            search_params["fields"] = fields

            docs = mpr.materials.summary.search(**search_params)

            results = []
            for doc in docs:
                doc_dict = serialize_object(doc)
                result = {
                    "material_id": doc_dict.get("material_id"),
                    "formula": doc_dict.get("formula_pretty"),
                    "band_gap": doc_dict.get("band_gap"),
                    "energy_above_hull": doc_dict.get("energy_above_hull"),
                    "is_stable": doc_dict.get("is_stable"),
                    "is_metal": doc_dict.get("is_metal"),
                    "formation_energy": doc_dict.get("formation_energy_per_atom"),
                    "density": doc_dict.get("density"),
                    "space_group": doc_dict.get("symmetry", {}).get("symbol") if isinstance(doc_dict.get("symmetry"), dict) else None
                }
                results.append(result)

            return {
                "status": "success",
                "count": len(results),
                "query": {k: str(v) for k, v in search_params.items() if k != "fields"},
                "results": results,
                "timestamp": datetime.now().isoformat()
            }

    except Exception as e:
        return {
            "error": str(e),
            "status": "error",
            "timestamp": datetime.now().isoformat()
        }


def main():
    parser = argparse.ArgumentParser(
        description="Search Materials Project database",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Search by material ID
  python materials_search.py --material-id mp-149

  # Search by formula
  python materials_search.py --formula Si

  # Search by elements
  python materials_search.py --elements Li,Fe,O --stable

  # Search semiconductors
  python materials_search.py --band-gap-min 1.0 --band-gap-max 3.0 --stable

  # Search magnetic materials
  python materials_search.py --elements Fe,O --magnetic --limit 5
        """
    )

    parser.add_argument("--material-id", help="Material ID (e.g., mp-149)")
    parser.add_argument("--formula", help="Chemical formula (e.g., Si, Fe2O3)")
    parser.add_argument("--elements", help="Comma-separated elements (e.g., Li,Fe,O)")
    parser.add_argument("--chemsys", help="Chemical system (e.g., Li-Fe-O)")
    parser.add_argument("--band-gap-min", type=float, help="Minimum band gap (eV)")
    parser.add_argument("--band-gap-max", type=float, help="Maximum band gap (eV)")
    parser.add_argument("--stable", action="store_true", help="Only stable materials")
    parser.add_argument("--metal", action="store_true", help="Only metallic materials")
    parser.add_argument("--magnetic", action="store_true", help="Only magnetic materials")
    parser.add_argument("--limit", type=int, default=10, help="Maximum results (default: 10)")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")

    args = parser.parse_args()

    # If no arguments provided, show help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    result = search_materials(args)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        # Pretty print for human reading
        if result.get("status") == "error":
            print(f"❌ Error: {result.get('error')}")
            sys.exit(1)

        print(f"\n🔍 Materials Search Results")
        print(f"{'='*60}")
        print(f"Found {result['count']} materials\n")

        for i, mat in enumerate(result['results'], 1):
            print(f"[{i}] {mat['formula']} ({mat['material_id']})")
            print(f"    Band Gap: {mat['band_gap']} eV")
            print(f"    E_hull: {mat['energy_above_hull']} eV/atom")
            print(f"    Stable: {mat['is_stable']}")
            print(f"    Space Group: {mat['space_group']}")
            print()


if __name__ == "__main__":
    main()
