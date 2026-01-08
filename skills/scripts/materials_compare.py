#!/usr/bin/env python3
"""
Materials Compare CLI - Compare multiple materials side by side
Usage: python materials_compare.py mp-149 mp-2534 mp-390
"""

import os
import sys
import json
import argparse
from datetime import datetime

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


def compare_materials(material_ids):
    """Compare multiple materials"""
    api_key = os.environ.get("MP_API_KEY")
    if not api_key:
        return {
            "error": "MP_API_KEY environment variable not set",
            "status": "error"
        }

    try:
        with MPRester(api_key) as mpr:
            fields = [
                "material_id", "formula_pretty", "band_gap", "energy_above_hull",
                "is_stable", "is_metal", "is_magnetic", "formation_energy_per_atom",
                "density", "volume", "nsites", "symmetry", "total_magnetization"
            ]

            docs = mpr.materials.summary.search(
                material_ids=material_ids,
                fields=fields
            )

            comparison = []
            for doc in docs:
                doc_dict = serialize_object(doc)
                symmetry = doc_dict.get('symmetry', {})

                # Handle crystal_system enum
                crystal_system = None
                if isinstance(symmetry, dict):
                    cs = symmetry.get('crystal_system')
                    if isinstance(cs, dict) and '_value_' in cs:
                        crystal_system = cs['_value_']
                    elif isinstance(cs, str):
                        crystal_system = cs

                result = {
                    "material_id": doc_dict.get("material_id"),
                    "formula": doc_dict.get("formula_pretty"),
                    "band_gap": doc_dict.get("band_gap"),
                    "is_metal": doc_dict.get("is_metal"),
                    "formation_energy": doc_dict.get("formation_energy_per_atom"),
                    "energy_above_hull": doc_dict.get("energy_above_hull"),
                    "is_stable": doc_dict.get("is_stable"),
                    "density": doc_dict.get("density"),
                    "volume": doc_dict.get("volume"),
                    "n_sites": doc_dict.get("nsites"),
                    "is_magnetic": doc_dict.get("is_magnetic"),
                    "magnetization": doc_dict.get("total_magnetization"),
                    "space_group": symmetry.get("symbol") if isinstance(symmetry, dict) else None,
                    "crystal_system": crystal_system,
                }
                comparison.append(result)

            return {
                "status": "success",
                "num_materials": len(comparison),
                "comparison": comparison,
                "timestamp": datetime.now().isoformat()
            }

    except Exception as e:
        return {
            "error": str(e),
            "status": "error",
            "timestamp": datetime.now().isoformat()
        }


def print_comparison_table(comparison):
    """Print comparison in horizontal table format"""
    if not comparison:
        return

    # Define properties to display
    properties = [
        ("Material_ID", "material_id", ""),
        ("Formula", "formula", ""),
        ("Band_Gap_eV", "band_gap", ""),
        ("Energy_Above_Hull", "energy_above_hull", " eV/atom"),
        ("Is_Stable", "is_stable", ""),
        ("Is_Metal", "is_metal", ""),
        ("Formation_Energy", "formation_energy", " eV/atom"),
        ("Density", "density", " g/cm³"),
        ("Volume", "volume", " Ų"),
        ("N_Sites", "n_sites", ""),
        ("Space_Group_Symbol", "space_group", ""),
        ("Crystal_System", "crystal_system", ""),
    ]

    # Calculate column widths
    prop_width = max(len(prop[0]) for prop in properties)
    col_widths = []

    for mat in comparison:
        formula = mat.get('formula', 'N/A')
        mat_id = mat.get('material_id', 'N/A')
        header = f"{formula} ({mat_id})"
        col_widths.append(max(20, len(header) + 2))

    # Print title
    print(f"\n合并文件包含{len(comparison)}个关键属性列:")

    # Print top border
    print("┌" + "─" * prop_width + "┬" + "┬".join("─" * w for w in col_widths) + "┐")

    # Print header row
    header_cells = []
    for mat in comparison:
        formula = mat.get('formula', 'N/A')
        mat_id = mat.get('material_id', 'N/A')
        header_cells.append(f"{formula} ({mat_id})")

    header_line = "│" + "属性".ljust(prop_width) + "│"
    for i, cell in enumerate(header_cells):
        header_line += cell.center(col_widths[i]) + "│"
    print(header_line)

    # Print separator after header
    print("├" + "─" * prop_width + "┼" + "┼".join("─" * w for w in col_widths) + "┤")

    # Print data rows
    for prop_name, prop_key, unit in properties:
        row = "│" + prop_name.ljust(prop_width) + "│"
        for i, mat in enumerate(comparison):
            value = mat.get(prop_key)
            if value is None:
                cell_value = "N/A"
            elif isinstance(value, bool):
                cell_value = str(value)
            elif isinstance(value, float):
                cell_value = f"{value:.4g}{unit}"
            else:
                cell_value = f"{value}{unit}"
            row += cell_value.center(col_widths[i]) + "│"
        print(row)

        # Print separator between rows
        if prop_name != properties[-1][0]:
            print("├" + "─" * prop_width + "┼" + "┼".join("─" * w for w in col_widths) + "┤")

    # Print bottom border
    print("└" + "─" * prop_width + "┴" + "┴".join("─" * w for w in col_widths) + "┘")
    print()


def main():
    parser = argparse.ArgumentParser(
        description="Compare multiple materials from Materials Project",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Compare two materials
  python materials_compare.py mp-149 mp-2534

  # Compare three materials
  python materials_compare.py mp-149 mp-2534 mp-390

  # Output as JSON
  python materials_compare.py mp-149 mp-2534 --json
        """
    )

    parser.add_argument("material_ids", nargs="+", help="Material IDs to compare (e.g., mp-149 mp-2534)")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")

    args = parser.parse_args()

    if len(args.material_ids) < 2:
        print("❌ Error: Please provide at least 2 material IDs to compare")
        sys.exit(1)

    result = compare_materials(args.material_ids)

    if result.get("status") == "error":
        print(f"❌ Error: {result.get('error')}")
        sys.exit(1)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print_comparison_table(result['comparison'])


if __name__ == "__main__":
    main()
