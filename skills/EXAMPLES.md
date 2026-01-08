# Skills Usage Examples

## Basic Searches

### Search by Material ID
```bash
/materials-search --material-id mp-149
```
Output:
```
🔍 Materials Search Results
============================================================
Found 1 materials

[1] Si (mp-149)
    Band Gap: 0.6105 eV
    E_hull: 0.0 eV/atom
    Stable: True
    Space Group: Fd-3m
```

### Search by Formula
```bash
/materials-search --formula TiO2
```

### Search by Elements
```bash
/materials-search --elements Li,Fe,O --stable --limit 5
```

## Advanced Searches

### Find Semiconductors
```bash
# Band gap between 1.0 and 3.0 eV
/materials-search --band-gap-min 1.0 --band-gap-max 3.0 --stable --limit 10
```

### Find Magnetic Materials
```bash
/materials-search --elements Fe,O --magnetic --stable
```

### Find Metals
```bash
/materials-search --elements Cu,Ag,Au --metal --limit 5
```

### Search Chemical System
```bash
/materials-search --chemsys Li-Fe-O --stable
```

## Export to Excel

### Export Single Material
```bash
/materials-export --material-id mp-149 --output silicon.xlsx
```
Output:
```
✅ Export successful!
📁 File: ./output/silicon.xlsx
📊 Materials: 1
```

### Export Search Results
```bash
# Export all stable semiconductors
/materials-export --band-gap-min 1.5 --band-gap-max 3.0 --stable --limit 50 --output semiconductors.xlsx
```

### Export Magnetic Materials
```bash
/materials-export --elements Fe,O --magnetic --stable --limit 30 --output magnetic_fe_o.xlsx
```

### Custom Output Directory
```bash
/materials-export --formula Si --output-dir ~/my_materials --output silicon_data.xlsx
```

## Compare Materials

### Compare Two Materials
```bash
/materials-compare mp-149 mp-2534
```
Output:
```
📊 Materials Comparison
================================================================================

[1] Si (mp-149)
    ──────────────────────────────────────────────────────────────────────
    Band Gap:          0.6105 eV
    Is Metal:          False
    Formation Energy:  0.0 eV/atom
    E above hull:      0.0 eV/atom
    Stable:            True
    Density:           2.31 g/cm³
    Volume:            40.33 Ų
    Sites:             2
    Magnetic:          False
    Space Group:       Fd-3m
    Crystal System:    Cubic

[2] GaAs (mp-2534)
    ──────────────────────────────────────────────────────────────────────
    Band Gap:          0.19 eV
    Is Metal:          False
    Formation Energy:  -0.45 eV/atom
    E above hull:      0.0 eV/atom
    Stable:            True
    Density:           5.05 g/cm³
    Volume:            47.53 Ų
    Sites:             2
    Magnetic:          False
    Space Group:       F-43m
    Crystal System:    Cubic
```

### Compare Multiple Materials
```bash
/materials-compare mp-149 mp-2534 mp-390 mp-1234
```

### JSON Output for Scripting
```bash
/materials-compare mp-149 mp-2534 --json > comparison.json
```

## Workflow Examples

### Example 1: Research Workflow
```bash
# 1. Search for materials
/materials-search --elements Li,Co,O --stable --limit 10

# 2. Compare interesting ones
/materials-compare mp-1234 mp-5678 mp-9012

# 3. Export detailed data
/materials-export --material-id mp-1234,mp-5678,mp-9012 --output li_co_o_comparison.xlsx
```

### Example 2: Semiconductor Research
```bash
# Find wide bandgap semiconductors
/materials-search --band-gap-min 2.5 --band-gap-max 4.0 --stable --limit 20

# Export for analysis
/materials-export --band-gap-min 2.5 --band-gap-max 4.0 --stable --limit 50 --output wide_bandgap.xlsx
```

### Example 3: Magnetic Materials Study
```bash
# Search magnetic iron compounds
/materials-search --elements Fe --magnetic --stable --limit 15

# Export with specific elements
/materials-export --elements Fe,O --magnetic --stable --limit 100 --output magnetic_iron_oxides.xlsx
```

### Example 4: Material Screening
```bash
# Screen for specific properties
/materials-search --elements Si,Ge --band-gap-min 0.5 --band-gap-max 1.5 --stable

# Compare candidates
/materials-compare mp-149 mp-157 mp-32

# Export finalists
/materials-export --material-id mp-149,mp-157 --output si_ge_finalists.xlsx
```

## Scripting with Skills

### Bash Script Example
```bash
#!/bin/bash
# Search and export materials

ELEMENTS="Li,Fe,O"
OUTPUT_DIR="./results"

# Create output directory
mkdir -p $OUTPUT_DIR

# Search
echo "Searching for $ELEMENTS materials..."
/materials-search --elements $ELEMENTS --stable --limit 10

# Export
echo "Exporting to Excel..."
/materials-export --elements $ELEMENTS --stable --limit 50 \
  --output-dir $OUTPUT_DIR \
  --output "${ELEMENTS}_materials.xlsx"

echo "Done! Check $OUTPUT_DIR"
```

### Python Integration
```python
import subprocess
import json

# Run search and get JSON output
result = subprocess.run(
    ["python", "skills/scripts/materials_search.py",
     "--formula", "Si", "--json"],
    capture_output=True,
    text=True
)

data = json.loads(result.stdout)
print(f"Found {data['count']} materials")

for mat in data['results']:
    print(f"{mat['formula']}: {mat['band_gap']} eV")
```

## Tips and Tricks

### 1. Use JSON for Automation
```bash
# Get JSON output
/materials-search --formula Si --json > si_data.json

# Process with jq
cat si_data.json | jq '.results[0].band_gap'
```

### 2. Chain Commands
```bash
# Search, then export based on results
/materials-search --elements Fe,O --magnetic --limit 5
# Review results, then:
/materials-export --elements Fe,O --magnetic --limit 50 --output fe_o.xlsx
```

### 3. Create Aliases
```bash
# Add to ~/.bashrc or ~/.zshrc
alias mat-search='/materials-search'
alias mat-export='/materials-export'
alias mat-compare='/materials-compare'

# Use shorter commands
mat-search --formula Si
```

### 4. Batch Processing
```bash
# Compare multiple sets
for id in mp-149 mp-2534 mp-390; do
  /materials-export --material-id $id --output "${id}.xlsx"
done
```

### 5. Save Common Queries
```bash
# Create a queries file
cat > my_queries.sh <<'EOF'
#!/bin/bash
# My common materials queries

# Semiconductors
alias find-semiconductors='/materials-search --band-gap-min 1.0 --band-gap-max 3.0 --stable'

# Magnetic materials
alias find-magnetic='/materials-search --magnetic --stable'

# Export template
alias export-mat='/materials-export --output-dir ~/materials_data'
EOF

source my_queries.sh
find-semiconductors --limit 10
```

## Error Handling

### Handle Missing API Key
```bash
if [ -z "$MP_API_KEY" ]; then
  echo "Error: MP_API_KEY not set"
  echo "Get your key from https://materialsproject.org/api"
  exit 1
fi

/materials-search --formula Si
```

### Check for Dependencies
```bash
# Check if dependencies are installed
python -c "import mp_api, pandas, openpyxl" 2>/dev/null
if [ $? -ne 0 ]; then
  echo "Installing dependencies..."
  pip install mp-api pandas openpyxl
fi
```

## Performance Tips

1. **Limit Results**: Use `--limit` to control result count
2. **Specific Queries**: More specific queries are faster
3. **JSON Output**: Use `--json` for programmatic access
4. **Batch Exports**: Export multiple materials in one call

## Next Steps

- See [README.md](README.md) for full documentation
- Check [INSTALL.md](INSTALL.md) for installation help
- Visit [Materials Project](https://materialsproject.org/) for more info
