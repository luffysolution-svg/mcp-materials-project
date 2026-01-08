# Materials Project Skills for Claude Code

Claude Code skills for querying the Materials Project database directly from your terminal using slash commands.

## 🚀 Features

Three powerful skills for materials science research:

- **`/materials-search`** - Search materials by formula, elements, band gap, and properties
- **`/materials-export`** - Export materials data to professionally formatted Excel files
- **`/materials-compare`** - Compare multiple materials side by side

## 📦 Installation

### Quick Install (Recommended) ⭐

Use the automated installer for correct SKILL.md format:

**Windows:**
```cmd
cd mcp-materials-project
skills\install-skills-windows.bat
```

**Linux/macOS:**
```bash
cd mcp-materials-project
chmod +x skills/install-skills-unix.sh
./skills/install-skills-unix.sh
```

This installs skills in the **correct Claude Code format**:
- Creates `~/.claude/skills/materials-xxx/` directories
- Copies `SKILL.md` files (required by Claude Code)
- Copies Python scripts
- Skills available in **all projects**!

**Important**: Restart Claude Code after installation to load the skills.

---

### Manual Installation

### Prerequisites

```bash
# Install required Python packages
pip install mp-api pandas openpyxl
```

### Setup

1. **Clone this repository:**
   ```bash
   git clone https://github.com/luffysolution-svg/mcp-materials-project.git
   cd mcp-materials-project
   ```

2. **Get your Materials Project API key:**
   - Visit https://materialsproject.org/api
   - Sign up/login and copy your API key

3. **Set environment variable:**
   ```bash
   # Windows
   set MP_API_KEY=your_api_key_here

   # Linux/macOS
   export MP_API_KEY=your_api_key_here
   ```

4. **Install skills:**

   **Option A: Project-level (recommended for testing)**
   ```bash
   # Skills will be available only in this project
   cp skills/skills.json .claude/skills.json
   ```

   **Option B: Global (available everywhere)**
   ```bash
   # Windows
   copy skills\skills.json %USERPROFILE%\.claude\skills.json

   # Linux/macOS
   cp skills/skills.json ~/.claude/skills.json
   ```

## 📖 Usage

### 1. Materials Search

Search the Materials Project database with various filters:

```bash
# Search by material ID
/materials-search --material-id mp-149

# Search by formula
/materials-search --formula Si

# Search by elements
/materials-search --elements Li,Fe,O --stable

# Search semiconductors (band gap 1-3 eV)
/materials-search --band-gap-min 1.0 --band-gap-max 3.0 --stable

# Search magnetic materials
/materials-search --elements Fe,O --magnetic --limit 10
```

**Options:**
- `--material-id` - Material ID (e.g., mp-149)
- `--formula` - Chemical formula (e.g., Si, Fe2O3)
- `--elements` - Comma-separated elements (e.g., Li,Fe,O)
- `--chemsys` - Chemical system (e.g., Li-Fe-O)
- `--band-gap-min` - Minimum band gap (eV)
- `--band-gap-max` - Maximum band gap (eV)
- `--stable` - Only stable materials
- `--metal` - Only metallic materials
- `--magnetic` - Only magnetic materials
- `--limit` - Maximum results (default: 10)
- `--json` - Output raw JSON

### 2. Materials Export

Export materials data to Excel with professional formatting:

```bash
# Export specific material
/materials-export --material-id mp-149 --output silicon.xlsx

# Export semiconductors
/materials-export --band-gap-min 1.0 --band-gap-max 3.0 --stable --limit 20

# Export magnetic materials
/materials-export --elements Fe,O --magnetic --output magnetic_materials.xlsx

# Export to custom directory
/materials-export --formula Si --output-dir ./my_exports
```

**Options:**
- Same search options as `/materials-search`
- `--output` / `-o` - Output filename (without path)
- `--output-dir` - Output directory (default: ./output)

**Excel Features:**
- Professional styling with headers and borders
- Auto-sized columns
- Frozen panes for easy navigation
- Auto-filter enabled
- Priority column ordering

### 3. Materials Compare

Compare multiple materials side by side:

```bash
# Compare two materials
/materials-compare mp-149 mp-2534

# Compare three materials
/materials-compare mp-149 mp-2534 mp-390

# Output as JSON
/materials-compare mp-149 mp-2534 --json
```

**Comparison includes:**
- Band gap
- Formation energy
- Energy above hull
- Stability
- Density and volume
- Magnetic properties
- Crystal structure
- Space group

## 🎯 Examples

### Example 1: Find and export stable semiconductors

```bash
# First, search to see what's available
/materials-search --band-gap-min 1.5 --band-gap-max 3.0 --stable --limit 5

# Then export to Excel
/materials-export --band-gap-min 1.5 --band-gap-max 3.0 --stable --limit 20 --output semiconductors.xlsx
```

### Example 2: Compare silicon polymorphs

```bash
# Search for silicon materials
/materials-search --formula Si --limit 5

# Compare specific ones
/materials-compare mp-149 mp-157
```

### Example 3: Research magnetic materials

```bash
# Search magnetic iron oxides
/materials-search --elements Fe,O --magnetic --stable --limit 10

# Export for further analysis
/materials-export --elements Fe,O --magnetic --stable --limit 50 --output fe_o_magnetic.xlsx
```

## 🔧 Troubleshooting

### Skills not showing up

1. Check that `skills.json` is in the correct location:
   - Project: `.claude/skills.json`
   - Global: `~/.claude/skills.json`

2. Restart Claude Code

3. Verify the file paths in `skills.json` are correct

### API Key errors

```bash
# Verify your API key is set
echo $MP_API_KEY  # Linux/macOS
echo %MP_API_KEY%  # Windows

# If not set, add to your shell profile:
# ~/.bashrc, ~/.zshrc, or ~/.bash_profile
export MP_API_KEY=your_api_key_here
```

### Import errors

```bash
# Reinstall dependencies
pip install --upgrade mp-api pandas openpyxl
```

## 📚 Data Fields

### Search Results Include:
- Material ID
- Chemical formula
- Band gap (eV)
- Energy above hull (eV/atom)
- Stability status
- Metallic/non-metallic
- Formation energy (eV/atom)
- Density (g/cm³)
- Space group

### Excel Export Includes:
All search fields plus:
- Volume (ų)
- Number of sites
- Elements list
- Space group number
- Crystal system

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Test your changes
4. Submit a pull request

## 📄 License

MIT License - see [LICENSE](../LICENSE) file for details

## 🔗 Links

- **GitHub**: https://github.com/luffysolution-svg/mcp-materials-project
- **Materials Project**: https://materialsproject.org/
- **API Documentation**: https://docs.materialsproject.org/

## 💡 Tips

1. **Use `--json` for scripting**: Pipe output to `jq` or other tools
2. **Combine with other tools**: Export to Excel, then analyze with pandas
3. **Save common queries**: Create shell aliases for frequent searches
4. **Batch processing**: Use shell loops to process multiple materials

## 🆘 Support

- **Issues**: https://github.com/luffysolution-svg/mcp-materials-project/issues
- **Materials Project Help**: https://matsci.org/materials-project

---

Made with ❤️ for materials science research
