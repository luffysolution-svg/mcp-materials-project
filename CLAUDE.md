# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a dual-purpose Materials Project integration:
1. **MCP Server** (`mcp_materials.py`) - FastMCP server exposing 6 tools for AI assistants
2. **CLI Skills** (`skills/scripts/`) - Standalone Python scripts for terminal use via Claude Code Skills

Both access the Materials Project database via `mp-api` but serve different use cases:
- MCP: Deep research with 60+ material properties, JSON output for AI parsing
- Skills: Quick comparisons with 14 core properties, human-friendly terminal output

## Environment Setup

**Required Environment Variable:**
```bash
export MP_API_KEY=your_api_key_here  # Get from https://materialsproject.org/api
```

**Dependencies:**
```bash
pip install -r requirements.txt
# Core: fastmcp, mp-api, pymatgen, pandas, openpyxl
```

## Development Commands

### Testing MCP Server
```bash
# Run server directly
python mcp_materials.py

# Or via entry point
mcp-materials-project

# Test with MCP inspector
mcp dev mcp_materials.py
```

### Testing CLI Scripts
```bash
# Search materials
python skills/scripts/materials_search.py --formula Si --limit 5

# Compare materials (outputs horizontal table)
python skills/scripts/materials_compare.py mp-390 mp-672

# Export to Excel (horizontal comparison format for multiple materials)
python skills/scripts/materials_export.py --material-ids mp-390,mp-672 --output test.xlsx
```

### Building and Publishing
```bash
# Build package
python -m build

# Publish to PyPI
twine upload dist/*

# Version is in pyproject.toml [project] version field
```

## Architecture

### Two Parallel Implementations

**1. MCP Server (`mcp_materials.py` - 845 lines)**
- **Framework**: FastMCP with `@mcp.tool` decorators
- **Data Model**: 60+ fields from `SUMMARY_FIELDS` constant (lines 84-150)
- **Processing**: `process_material_doc()` flattens nested structures into 60+ columns
- **Excel Format**: Vertical (rows=materials, cols=properties), suitable for many materials
- **Tools**:
  - `fetch_full_material_data()` - Main search with all fields
  - `get_structure_details()` - Crystal structure with lattice/atomic positions
  - `search_materials_by_property()` - Property range queries
  - `get_phase_diagram_info()` - Phase diagram data
  - `compare_materials()` - Side-by-side comparison
  - `export_to_excel()` - Full data export

**2. CLI Skills (`skills/scripts/` - 850 lines total)**
- **Framework**: Standalone argparse scripts
- **Data Model**: 14 core fields (Material_ID, Formula, Band_Gap, etc.)
- **Processing**: Minimal field extraction for speed
- **Excel Format**: Horizontal (rows=properties, cols=materials), ideal for 2-10 material comparison
- **Scripts**:
  - `materials_search.py` - Basic search, emoji output
  - `materials_compare.py` - Unicode table comparison
  - `materials_export.py` - Dual format (vertical for single, horizontal for multiple)

### Key Architectural Decisions

**Why Two Implementations?**
- MCP: Comprehensive data for research (弹性模量, 介电常数, 表面能)
- Skills: Fast terminal workflow with visual tables

**Excel Export Logic** (`materials_export.py:324-352`):
```python
use_comparison_format = args.material_ids and len(materials_data) >= 2

if use_comparison_format:
    create_comparison_excel()  # Horizontal: 属性 | TiO2 | CdS
else:
    # Traditional vertical format
```

**Horizontal Table Rendering** (`materials_compare.py:113-187`):
- Uses Unicode box-drawing characters (┌─┬─┐)
- Chinese title: "合并文件包含N个关键属性列"
- Auto-calculates column widths
- Properties in first column, materials in subsequent columns

**MPID Comparison Bug Fix** (`materials_export.py:170`):
```python
# CRITICAL: Check None first to avoid MPID.__eq__ triggering
if value is None or value == '':  # Wrong - triggers MPID validation
if value is None:                  # Correct - safe check
```

### Data Serialization

**Common Pattern** (both implementations):
```python
def serialize_object(obj):
    # Handles: pymatgen objects, numpy arrays, nested dicts
    # Converts enums (CrystalSystem) to strings
    # Flattens structure objects
```

**MCP Flattening** (`mcp_materials.py:52-80`):
```python
flatten_dict(d, parent_key='', sep='_')
# symmetry.crystal_system -> Symmetry_Crystal_System
# Handles nested dicts, lists, matrices
```

**Skills Extraction** (`materials_export.py:52-91`):
```python
process_material_doc(doc)
# Extracts only 14 fields
# Handles crystal_system enum: cs['_value_'] or str(cs)
```

## Skills Installation

Skills use `SKILL.md` format (not `skills.json`):
```
~/.claude/skills/
  materials-search/SKILL.md
  materials-export/SKILL.md
  materials-compare/SKILL.md
```

**Automated Install:**
```bash
# Windows
skills\install-skills-windows.bat

# Unix
./skills/install-skills-unix.sh
```

**SKILL.md Structure:**
- Metadata: name, description, version
- Prerequisites: Repository clone instructions
- Script location: Relative path from repo root
- Usage examples with actual commands

**Path Handling**: Skills reference `<repo_path>/skills/scripts/` to avoid hardcoded paths.

## Common Patterns

### API Query Construction
```python
search_params = {}
if material_ids:
    search_params["material_ids"] = [mid.strip() for mid in ids.split(",")]
# Don't add chunk_size when using material_ids (causes API error)
if not material_ids:
    search_params["num_chunks"] = 1
    search_params["chunk_size"] = limit
```

### Excel Styling
```python
# MCP: Basic blue header (#DDEBF7)
# Skills: Professional dark blue (#366092) + white text
# Both: Borders, frozen panes, auto-filter, auto-width
```

### Error Handling
```python
# MCP: Returns JSON with status/error/timestamp
# Skills: Prints emoji (❌) + error message, exits with code 1
```

## Testing Workflow

1. **Test MCP tool**: Verify JSON output structure
2. **Test CLI script**: Check terminal table rendering
3. **Test Excel export**:
   - Single material → vertical format
   - Multiple materials → horizontal comparison
4. **Verify SKILL.md**: Check paths are relative, not hardcoded

## Git Workflow

**Commit Message Format:**
```
Brief description

Major improvements:
1. Feature A
2. Feature B

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

**Files to Commit:**
- `mcp_materials.py` - MCP server
- `skills/scripts/*.py` - CLI scripts
- `skills/skill-definitions/*.SKILL.md` - Skill definitions (if updated)
- `pyproject.toml` - Version bumps
- `README.md` - Documentation updates

**Files to Ignore:**
- `output/*.xlsx` - Test Excel files
- `dist/*` - Build artifacts (committed only for releases)
- `.claude/` - Local configuration

## Version Management

Version is defined in:
- `pyproject.toml` line 7: `version = "0.2.0"`
- `smithery.json` line 5: `"version": "0.2.0"`
- Update both when releasing

Current: v0.2.0 (added Excel export, environment variable API key)
