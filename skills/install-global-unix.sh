#!/bin/bash
# Materials Project Skills - Global Installation Script for Linux/macOS
# This script installs the skills globally for all projects

set -e

echo "========================================"
echo "Materials Project Skills Installer"
echo "========================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 is not installed"
    echo "Please install Python 3.10+ from https://www.python.org/"
    exit 1
fi

echo "[1/5] Checking Python installation..."
python3 --version
echo ""

# Check if MP_API_KEY is set
if [ -z "$MP_API_KEY" ]; then
    echo "[WARNING] MP_API_KEY environment variable is not set"
    echo ""
    echo "Please set your Materials Project API key:"
    echo "  1. Get your key from https://materialsproject.org/api"
    echo "  2. Add to your shell profile (~/.bashrc or ~/.zshrc):"
    echo "     export MP_API_KEY=\"your_api_key_here\""
    echo "  3. Run: source ~/.bashrc (or ~/.zshrc)"
    echo ""
    read -p "Continue anyway? (y/n): " CONTINUE
    if [ "$CONTINUE" != "y" ]; then
        exit 1
    fi
    echo ""
fi

# Install dependencies
echo "[2/5] Installing Python dependencies..."
pip3 install mp-api pandas openpyxl
echo ""

# Create global directory
echo "[3/5] Creating global directory..."
GLOBAL_DIR="$HOME/.claude/materials-skills"
mkdir -p "$GLOBAL_DIR/scripts"
echo "Created: $GLOBAL_DIR"
echo ""

# Copy scripts
echo "[4/5] Copying scripts..."
cp skills/scripts/materials_search.py "$GLOBAL_DIR/scripts/"
cp skills/scripts/materials_export.py "$GLOBAL_DIR/scripts/"
cp skills/scripts/materials_compare.py "$GLOBAL_DIR/scripts/"
chmod +x "$GLOBAL_DIR/scripts/"*.py
echo "Copied 3 scripts to $GLOBAL_DIR/scripts/"
echo ""

# Create global skills.json
echo "[5/5] Creating global skills configuration..."
cat > "$HOME/.claude/skills.json" <<EOF
{
  "skills": {
    "materials-search": {
      "name": "Materials Search",
      "description": "Search Materials Project database for materials by formula, elements, band gap, and other properties",
      "command": "python3",
      "args": [
        "$GLOBAL_DIR/scripts/materials_search.py"
      ],
      "env": {
        "MP_API_KEY": "\${env:MP_API_KEY}",
        "PYTHONPATH": "$GLOBAL_DIR"
      },
      "category": "materials",
      "icon": "search"
    },
    "materials-export": {
      "name": "Materials Export",
      "description": "Export materials data to professionally formatted Excel files",
      "command": "python3",
      "args": [
        "$GLOBAL_DIR/scripts/materials_export.py"
      ],
      "env": {
        "MP_API_KEY": "\${env:MP_API_KEY}",
        "PYTHONPATH": "$GLOBAL_DIR"
      },
      "category": "materials",
      "icon": "download"
    },
    "materials-compare": {
      "name": "Materials Compare",
      "description": "Compare multiple materials side by side with detailed property comparison",
      "command": "python3",
      "args": [
        "$GLOBAL_DIR/scripts/materials_compare.py"
      ],
      "env": {
        "MP_API_KEY": "\${env:MP_API_KEY}",
        "PYTHONPATH": "$GLOBAL_DIR"
      },
      "category": "materials",
      "icon": "compare"
    }
  }
}
EOF

echo "Created: $HOME/.claude/skills.json"
echo ""

# Test installation
echo "========================================"
echo "Testing installation..."
echo "========================================"
python3 "$GLOBAL_DIR/scripts/materials_search.py" --help > /dev/null 2>&1

echo ""
echo "========================================"
echo "Installation Complete!"
echo "========================================"
echo ""
echo "Skills installed globally at:"
echo "  $GLOBAL_DIR"
echo ""
echo "Configuration file:"
echo "  $HOME/.claude/skills.json"
echo ""
echo "Available skills:"
echo "  /materials-search  - Search materials database"
echo "  /materials-export  - Export to Excel"
echo "  /materials-compare - Compare materials"
echo ""
echo "Usage examples:"
echo "  /materials-search --formula Si"
echo "  /materials-export --band-gap-min 1.0 --band-gap-max 3.0 --stable"
echo "  /materials-compare mp-149 mp-2534"
echo ""
echo "Note: Restart Claude Code to load the new skills"
echo ""
