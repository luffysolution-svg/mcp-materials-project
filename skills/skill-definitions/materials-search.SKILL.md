---
name: materials-search
description: |
  Search Materials Project database for materials by formula, elements, band gap, and other properties.
  Returns structured data with material properties including band gap, stability, crystal structure, and more.
version: 1.0.0
---

# 🔬 Materials Project Search Protocol

## 🎯 Core Capabilities
1. **Multi-criteria Search**: Search by formula, elements, chemical system, band gap, stability, magnetic properties
2. **Property Filtering**: Filter by band gap ranges, stability, metallic/non-metallic, magnetic properties
3. **Structured Output**: Returns JSON or formatted text with key material properties

## 📋 Execution Instructions

### 1. Search Parameters
Available search criteria:
- **Material ID**: Direct lookup (e.g., mp-149)
- **Formula**: Chemical formula (e.g., Si, Fe2O3, TiO2)
- **Elements**: Comma-separated elements (e.g., Li,Fe,O)
- **Chemical System**: Element system (e.g., Li-Fe-O)
- **Band Gap**: Min/max range in eV
- **Stability**: Only stable materials (is_stable=true)
- **Metallic**: Only metals (is_metal=true)
- **Magnetic**: Only magnetic materials (is_magnetic=true)

### 2. Tool Invocation
When user requests materials search, execute:

```bash
python C:\Users\CSC\.claude\materials-skills\scripts\materials_search.py [OPTIONS]
```

**Required Environment**: MP_API_KEY must be set

**Common Options**:
- `--material-id mp-149` - Search by ID
- `--formula Si` - Search by formula
- `--elements Li,Fe,O` - Search by elements
- `--band-gap-min 1.0 --band-gap-max 3.0` - Band gap range
- `--stable` - Only stable materials
- `--metal` - Only metals
- `--magnetic` - Only magnetic materials
- `--limit 10` - Maximum results (default: 10)
- `--json` - Output as JSON

### 3. Output Format

**Standard Output** (Human-readable):
```
🔍 Materials Search Results
============================================================
Found N materials

[1] Formula (material-id)
    Band Gap: X.XX eV
    E_hull: X.XX eV/atom
    Stable: True/False
    Space Group: Symbol
```

**JSON Output** (for scripting):
```json
{
  "status": "success",
  "count": N,
  "results": [
    {
      "material_id": "mp-149",
      "formula": "Si",
      "band_gap": 0.6105,
      "energy_above_hull": 0.0,
      "is_stable": true,
      "space_group": "Fd-3m"
    }
  ]
}
```

## 🎯 Usage Examples

### Example 1: Search by Formula
**User**: "Search for silicon materials"
**Command**: `--formula Si`
**Output**: Returns all silicon polymorphs with properties

### Example 2: Find Semiconductors
**User**: "Find stable semiconductors with band gap 1-3 eV"
**Command**: `--band-gap-min 1.0 --band-gap-max 3.0 --stable --limit 10`
**Output**: Returns top 10 stable semiconductors in range

### Example 3: Search Magnetic Materials
**User**: "Find magnetic iron oxide materials"
**Command**: `--elements Fe,O --magnetic --stable`
**Output**: Returns stable magnetic Fe-O compounds

### Example 4: Search by Material ID
**User**: "Get properties of mp-149"
**Command**: `--material-id mp-149`
**Output**: Returns detailed properties of Silicon (mp-149)

## 📦 Data Fields Returned

- **Material_ID**: Materials Project identifier
- **Formula**: Chemical formula
- **Band_Gap**: Band gap in eV
- **Energy_Above_Hull**: Stability metric (eV/atom)
- **Is_Stable**: Thermodynamic stability
- **Is_Metal**: Metallic character
- **Formation_Energy**: Formation energy (eV/atom)
- **Density**: Density (g/cm³)
- **Space_Group**: Crystal symmetry

## 🛠 Error Handling

- **No API Key**: Returns error message with instructions
- **No Results**: Returns empty results with query parameters
- **Invalid Parameters**: Shows help message with valid options

## 🔄 Integration with Other Skills

Can be combined with:
- `/materials-export` - Export search results to Excel
- `/materials-compare` - Compare found materials

## 📝 Response Protocol

1. **Parse user query** to identify search criteria
2. **Construct command** with appropriate parameters
3. **Execute search** via Python script
4. **Format results** for user readability
5. **Suggest follow-up** actions (export, compare, refine search)
