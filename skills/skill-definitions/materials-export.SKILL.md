---
name: materials-export
description: |
  Export materials data to professionally formatted Excel files with auto-styling, filters, and priority column ordering.
  Supports all search criteria from materials-search plus custom output options.
version: 1.0.0
---

# 📊 Materials Export to Excel Protocol

## 🎯 Core Capabilities
1. **Professional Excel Export**: Auto-styled headers, borders, frozen panes, filters
2. **All Search Criteria**: Supports same filters as materials-search
3. **Custom Output**: Custom filenames and directories
4. **Batch Export**: Export multiple materials in one operation

## 📋 Execution Instructions

### 1. Export Parameters
All search parameters from materials-search PLUS:
- **--output / -o**: Custom filename (e.g., silicon.xlsx)
- **--output-dir**: Output directory (default: ./output)

### 2. Tool Invocation
When user requests Excel export, execute:

```bash
python ~/.claude/skills/materials-export/materials_export.py [OPTIONS]
```

**Note**: On Windows, use `%USERPROFILE%\.claude\skills\materials-export\materials_export.py`

**Required Environment**: MP_API_KEY must be set

**Common Options**:
- `--material-id mp-149 --output silicon.xlsx`
- `--formula Si --output-dir ~/materials`
- `--band-gap-min 1.0 --band-gap-max 3.0 --stable --limit 50`
- `--elements Li,Fe,O --magnetic --output battery_materials.xlsx`

### 3. Excel Features

**Automatic Styling**:
- Header row: Bold, blue background (#DDEBF7), centered
- Data cells: Top-aligned, wrapped text, bordered
- Column widths: Auto-sized (12-50 characters)
- Row height: 40-60 pixels for readability
- Frozen panes: First row and column
- Auto-filter: Enabled on all columns

**Column Priority Order**:
1. Material_ID
2. Formula
3. Band_Gap_eV
4. Energy_Above_Hull_eV_Atom
5. Space_Group_Symbol
6. Is_Stable
7. Is_Metal
8. Is_Magnetic
9. Formation_Energy_eV_Atom
10. Density_g_cm3
11. Volume_A3
12. Crystal_System
13. N_Sites
14. Elements
15. (Additional properties...)

### 4. Output Format

**Success Response**:
```
✅ Export successful!
📁 File: ./output/silicon.xlsx
📊 Materials: 1
```

**Error Response**:
```
❌ Error: [error message]
```

## 🎯 Usage Examples

### Example 1: Export Single Material
**User**: "Export mp-149 to Excel"
**Command**: `--material-id mp-149 --output silicon.xlsx`
**Result**: Creates silicon.xlsx with Silicon properties

### Example 2: Export Semiconductors
**User**: "Export all stable semiconductors with band gap 1.5-3 eV to Excel"
**Command**: `--band-gap-min 1.5 --band-gap-max 3.0 --stable --limit 50 --output semiconductors.xlsx`
**Result**: Creates semiconductors.xlsx with 50 materials

### Example 3: Export Battery Materials
**User**: "Export lithium cobalt oxide materials"
**Command**: `--elements Li,Co,O --stable --output battery_materials.xlsx`
**Result**: Creates battery_materials.xlsx with Li-Co-O compounds

### Example 4: Custom Directory
**User**: "Export iron oxides to my research folder"
**Command**: `--elements Fe,O --stable --output-dir ~/research/materials --output fe_o.xlsx`
**Result**: Creates ~/research/materials/fe_o.xlsx

## 📦 Excel Data Fields

**Core Properties**:
- Material_ID, Formula, Band_Gap_eV
- Energy_Above_Hull_eV_Atom, Is_Stable
- Formation_Energy_eV_Atom, Density_g_cm3

**Structure**:
- Space_Group_Symbol, Space_Group_Number
- Crystal_System, N_Sites, Elements

**Additional**:
- Volume_A3, Is_Metal, Is_Magnetic
- (All available properties from Materials Project)

## 🛠 Error Handling

- **No API Key**: Returns error with setup instructions
- **No Results**: Returns error "No materials found"
- **Invalid Path**: Creates directory if needed
- **File Exists**: Overwrites with confirmation

## 🔄 Workflow Integration

**Typical Workflow**:
1. User searches with `/materials-search`
2. Reviews results
3. Exports with `/materials-export` using same criteria
4. Opens Excel file for analysis

**Example**:
```
User: "Find stable semiconductors"
→ /materials-search --band-gap-min 1.0 --band-gap-max 3.0 --stable --limit 5
[Reviews 5 results]

User: "Export these to Excel"
→ /materials-export --band-gap-min 1.0 --band-gap-max 3.0 --stable --limit 50 --output semiconductors.xlsx
[Creates Excel with 50 materials]
```

## 📝 Response Protocol

1. **Parse user query** for search criteria and output preferences
2. **Construct command** with search + export parameters
3. **Execute export** via Python script
4. **Confirm success** with file path and count
5. **Suggest next steps** (open file, refine search, export more)
