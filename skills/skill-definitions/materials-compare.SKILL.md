---
name: materials-compare
description: |
  Compare multiple materials side by side with detailed property comparison.
  Shows band gap, formation energy, stability, density, magnetic properties, and crystal structure.
version: 1.0.0
---

# ⚖️ Materials Comparison Protocol

## 🎯 Core Capabilities
1. **Side-by-Side Comparison**: Compare 2-10 materials simultaneously
2. **Comprehensive Properties**: Band gap, energy, stability, structure, magnetism
3. **Formatted Output**: Human-readable table or JSON for scripting
4. **Quick Analysis**: Identify differences and similarities at a glance

## 📋 Execution Instructions

### 1. Comparison Parameters
**Required**: 2 or more Material IDs
**Optional**: --json for JSON output

### 2. Tool Invocation
When user requests material comparison, execute:

```bash
python C:\Users\CSC\.claude\materials-skills\scripts\materials_compare.py [MATERIAL_IDS] [OPTIONS]
```

**Required Environment**: MP_API_KEY must be set

**Usage**:
- `mp-149 mp-2534` - Compare two materials
- `mp-149 mp-2534 mp-390` - Compare three materials
- `mp-149 mp-2534 --json` - JSON output

### 3. Output Format

**Standard Output** (Human-readable):
```
📊 Materials Comparison
================================================================================

[1] Formula (material-id)
    ──────────────────────────────────────────────────────────────────────
    Band Gap:          X.XX eV
    Is Metal:          True/False
    Formation Energy:  X.XX eV/atom
    E above hull:      X.XX eV/atom
    Stable:            True/False
    Density:           X.XX g/cm³
    Volume:            X.XX Ų
    Sites:             N
    Magnetic:          True/False
    Space Group:       Symbol
    Crystal System:    System

[2] Formula (material-id)
    [Same format...]
```

**JSON Output** (for scripting):
```json
{
  "status": "success",
  "num_materials": 2,
  "comparison": [
    {
      "material_id": "mp-149",
      "formula": "Si",
      "band_gap": 0.6105,
      "is_metal": false,
      "formation_energy": 0.0,
      "energy_above_hull": 0.0,
      "is_stable": true,
      "density": 2.31,
      "volume": 40.33,
      "n_sites": 2,
      "is_magnetic": false,
      "space_group": "Fd-3m",
      "crystal_system": "Cubic"
    }
  ]
}
```

## 🎯 Usage Examples

### Example 1: Compare Two Materials
**User**: "Compare silicon and gallium arsenide"
**Command**: `mp-149 mp-2534`
**Output**: Side-by-side comparison of Si and GaAs

### Example 2: Compare Multiple Materials
**User**: "Compare mp-149, mp-2534, and mp-390"
**Command**: `mp-149 mp-2534 mp-390`
**Output**: Three-way comparison table

### Example 3: JSON Output
**User**: "Compare mp-149 and mp-2534 as JSON"
**Command**: `mp-149 mp-2534 --json`
**Output**: JSON format for scripting

### Example 4: Compare Polymorphs
**User**: "Compare different silicon structures"
**Command**: `mp-149 mp-157 mp-32`
**Output**: Comparison of Si polymorphs

## 📦 Comparison Fields

**Electronic Properties**:
- Band_Gap (eV)
- Is_Metal (boolean)
- Is_Gap_Direct (boolean)

**Thermodynamic Properties**:
- Formation_Energy (eV/atom)
- Energy_Above_Hull (eV/atom)
- Is_Stable (boolean)

**Physical Properties**:
- Density (g/cm³)
- Volume (ų)
- N_Sites (integer)

**Magnetic Properties**:
- Is_Magnetic (boolean)
- Total_Magnetization (μB)

**Structural Properties**:
- Space_Group (symbol)
- Crystal_System (name)

## 🛠 Error Handling

- **No API Key**: Returns error with setup instructions
- **Invalid Material ID**: Shows error for specific ID
- **Less than 2 IDs**: Prompts for at least 2 materials
- **Material Not Found**: Shows which IDs were not found

## 🔄 Workflow Integration

**Typical Workflow**:
1. User searches materials with `/materials-search`
2. Identifies interesting materials
3. Compares with `/materials-compare`
4. Exports detailed data with `/materials-export`

**Example**:
```
User: "Find stable semiconductors"
→ /materials-search --band-gap-min 1.0 --band-gap-max 2.0 --stable --limit 5
[Results: mp-149, mp-2534, mp-390, mp-1234, mp-5678]

User: "Compare the first three"
→ /materials-compare mp-149 mp-2534 mp-390
[Shows detailed comparison]

User: "Export mp-149 for detailed analysis"
→ /materials-export --material-id mp-149 --output silicon_detailed.xlsx
```

## 📝 Response Protocol

1. **Parse material IDs** from user query
2. **Validate count** (minimum 2 materials)
3. **Construct command** with IDs and options
4. **Execute comparison** via Python script
5. **Format results** for readability
6. **Highlight differences** in key properties
7. **Suggest follow-up** (export, search similar, refine)

## 💡 Analysis Tips

When presenting comparison results:
- **Highlight key differences** in band gap, stability, density
- **Note structural similarities** (same crystal system, space group)
- **Identify trends** (e.g., "All three are stable cubic structures")
- **Suggest applications** based on properties
- **Recommend further analysis** if needed
