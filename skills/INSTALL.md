# Quick Installation Guide for Skills

## 1. Install Dependencies

```bash
pip install mp-api pandas openpyxl
```

## 2. Get API Key

Visit https://materialsproject.org/api and get your free API key.

## 3. Set Environment Variable

**Windows:**
```cmd
setx MP_API_KEY "your_api_key_here"
```

**Linux/macOS:**
```bash
echo 'export MP_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc
```

## 4. Install Skills

**Option A: Clone Repository**
```bash
git clone https://github.com/luffysolution-svg/mcp-materials-project.git
cd mcp-materials-project
cp skills/skills.json .claude/skills.json
```

**Option B: Download Skills Only**
```bash
# Create directory
mkdir -p ~/.claude

# Download skills.json
curl -o ~/.claude/skills.json https://raw.githubusercontent.com/luffysolution-svg/mcp-materials-project/main/skills/skills.json

# Download scripts
mkdir -p ~/materials-skills/scripts
cd ~/materials-skills/scripts
curl -O https://raw.githubusercontent.com/luffysolution-svg/mcp-materials-project/main/skills/scripts/materials_search.py
curl -O https://raw.githubusercontent.com/luffysolution-svg/mcp-materials-project/main/skills/scripts/materials_export.py
curl -O https://raw.githubusercontent.com/luffysolution-svg/mcp-materials-project/main/skills/scripts/materials_compare.py
```

**Option C: Manual Setup**
1. Download `skills/skills.json` from GitHub
2. Download all scripts from `skills/scripts/`
3. Copy `skills.json` to `.claude/skills.json` in your project or home directory
4. Update paths in `skills.json` to point to your script locations

## 5. Verify Installation

```bash
# Test search
python skills/scripts/materials_search.py --material-id mp-149

# Should output material information for Silicon
```

## 6. Use in Claude Code

```bash
# Start Claude Code in your project
claude

# Use skills
/materials-search --formula Si
/materials-export --material-id mp-149 --output silicon.xlsx
/materials-compare mp-149 mp-2534
```

## Troubleshooting

### Skills not found
- Restart Claude Code after installing skills
- Check that `skills.json` is in `.claude/` directory
- Verify paths in `skills.json` are correct

### API Key errors
```bash
# Verify API key is set
echo $MP_API_KEY  # Linux/macOS
echo %MP_API_KEY%  # Windows
```

### Import errors
```bash
# Reinstall dependencies
pip install --upgrade mp-api pandas openpyxl
```

## Next Steps

See [skills/README.md](README.md) for detailed usage examples and all available options.
