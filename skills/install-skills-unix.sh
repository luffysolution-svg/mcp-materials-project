#!/bin/bash
# Materials Project Skills - Correct Installation for Claude Code
# Installs skills in SKILL.md format (the correct way)

set -e

echo "========================================"
echo "Materials Project Skills Installer"
echo "Claude Code SKILL.md Format"
echo "========================================"
echo ""

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "[ERROR] Python 3 not installed"
    exit 1
fi

echo "[1/6] Python version:"
python3 --version
echo ""

# Check API Key
if [ -z "$MP_API_KEY" ]; then
    echo "[WARNING] MP_API_KEY not set"
    echo "Get your key from https://materialsproject.org/api"
    echo "Add to ~/.bashrc or ~/.zshrc:"
    echo "  export MP_API_KEY=\"your_key_here\""
    echo ""
    read -p "Continue anyway? (y/n): " CONTINUE
    if [ "$CONTINUE" != "y" ]; then
        exit 1
    fi
fi

# Install dependencies
echo "[2/6] Installing dependencies..."
pip3 install mp-api pandas openpyxl
echo ""

# Create skill directories
echo "[3/6] Creating skill directories..."
SKILLS_DIR="$HOME/.claude/skills"
mkdir -p "$SKILLS_DIR/materials-search"
mkdir -p "$SKILLS_DIR/materials-export"
mkdir -p "$SKILLS_DIR/materials-compare"
echo "Created skill directories"
echo ""

# Copy SKILL.md files
echo "[4/6] Copying SKILL.md files..."
cp skills/skill-definitions/materials-search.SKILL.md "$SKILLS_DIR/materials-search/SKILL.md"
cp skills/skill-definitions/materials-export.SKILL.md "$SKILLS_DIR/materials-export/SKILL.md"
cp skills/skill-definitions/materials-compare.SKILL.md "$SKILLS_DIR/materials-compare/SKILL.md"
echo "Copied 3 SKILL.md files"
echo ""

# Copy Python scripts
echo "[5/6] Copying Python scripts..."
cp skills/scripts/materials_search.py "$SKILLS_DIR/materials-search/"
cp skills/scripts/materials_export.py "$SKILLS_DIR/materials-export/"
cp skills/scripts/materials_compare.py "$SKILLS_DIR/materials-compare/"
chmod +x "$SKILLS_DIR"/materials-*/*.py
echo "Copied 3 Python scripts"
echo ""

# Test
echo "[6/6] Testing installation..."
python3 "$SKILLS_DIR/materials-search/materials_search.py" --help > /dev/null 2>&1

echo ""
echo "========================================"
echo "Installation Complete!"
echo "========================================"
echo ""
echo "Skills installed at:"
echo "  $SKILLS_DIR/materials-search/"
echo "  $SKILLS_DIR/materials-export/"
echo "  $SKILLS_DIR/materials-compare/"
echo ""
echo "Each directory contains:"
echo "  - SKILL.md (skill definition)"
echo "  - Python script"
echo ""
echo "Available skills:"
echo "  /materials-search  - Search materials database"
echo "  /materials-export  - Export to Excel"
echo "  /materials-compare - Compare materials"
echo ""
echo "IMPORTANT: Restart Claude Code to load skills!"
echo ""
echo "Usage:"
echo "  /materials-search --formula Si"
echo "  /materials-export --material-id mp-149 --output silicon.xlsx"
echo "  /materials-compare mp-149 mp-2534"
echo ""
