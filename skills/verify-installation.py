#!/usr/bin/env python3
"""
Verify Materials Project Skills Global Installation
"""

import os
import sys
import json
from pathlib import Path

def check_mark(condition):
    return "✅" if condition else "❌"

def main():
    print("\n" + "="*60)
    print("Materials Project Skills - Installation Verification")
    print("="*60 + "\n")

    all_good = True

    # 1. Check Python version
    print("1. Python Version")
    py_version = sys.version_info
    py_ok = py_version >= (3, 10)
    print(f"   {check_mark(py_ok)} Python {py_version.major}.{py_version.minor}.{py_version.micro}")
    if not py_ok:
        print("   ⚠️  Python 3.10+ required")
        all_good = False
    print()

    # 2. Check dependencies
    print("2. Python Dependencies")
    deps = {
        "mp_api": "mp-api",
        "pandas": "pandas",
        "openpyxl": "openpyxl"
    }
    for module, package in deps.items():
        try:
            __import__(module)
            print(f"   ✅ {package}")
        except ImportError:
            print(f"   ❌ {package} - Run: pip install {package}")
            all_good = False
    print()

    # 3. Check API key
    print("3. Environment Variables")
    api_key = os.environ.get("MP_API_KEY")
    if api_key:
        print(f"   ✅ MP_API_KEY is set ({api_key[:10]}...)")
    else:
        print("   ❌ MP_API_KEY not set")
        print("      Get your key from https://materialsproject.org/api")
        all_good = False
    print()

    # 4. Check global directory
    print("4. Global Installation")
    home = Path.home()
    global_dir = home / ".claude" / "materials-skills"
    scripts_dir = global_dir / "scripts"

    if global_dir.exists():
        print(f"   ✅ Global directory: {global_dir}")
    else:
        print(f"   ❌ Global directory not found: {global_dir}")
        all_good = False

    # Check scripts
    scripts = ["materials_search.py", "materials_export.py", "materials_compare.py"]
    for script in scripts:
        script_path = scripts_dir / script
        if script_path.exists():
            print(f"   ✅ {script}")
        else:
            print(f"   ❌ {script} not found")
            all_good = False
    print()

    # 5. Check skills.json
    print("5. Skills Configuration")
    skills_json = home / ".claude" / "skills.json"
    if skills_json.exists():
        print(f"   ✅ skills.json: {skills_json}")
        try:
            with open(skills_json) as f:
                config = json.load(f)

            expected_skills = ["materials-search", "materials-export", "materials-compare"]
            for skill in expected_skills:
                if skill in config.get("skills", {}):
                    print(f"   ✅ /{skill}")
                else:
                    print(f"   ❌ /{skill} not configured")
                    all_good = False
        except Exception as e:
            print(f"   ❌ Error reading skills.json: {e}")
            all_good = False
    else:
        print(f"   ❌ skills.json not found: {skills_json}")
        all_good = False
    print()

    # 6. Test script execution
    print("6. Script Execution Test")
    test_script = scripts_dir / "materials_search.py"
    if test_script.exists():
        try:
            import subprocess
            result = subprocess.run(
                [sys.executable, str(test_script), "--help"],
                capture_output=True,
                timeout=30  # Increased timeout for mp-api loading
            )
            if result.returncode == 0:
                print("   ✅ Scripts are executable")
            else:
                print("   ❌ Script execution failed")
                all_good = False
        except Exception as e:
            print(f"   ❌ Error testing script: {e}")
            all_good = False
    else:
        print("   ⚠️  Cannot test - script not found")
    print()

    # Summary
    print("="*60)
    if all_good:
        print("✅ Installation verified successfully!")
        print("\nYou can now use:")
        print("  /materials-search --formula Si")
        print("  /materials-export --material-id mp-149 --output silicon.xlsx")
        print("  /materials-compare mp-149 mp-2534")
    else:
        print("❌ Installation has issues - please fix the errors above")
        print("\nRun the installer again:")
        print("  Windows: skills\\install-global-windows.bat")
        print("  Unix:    ./skills/install-global-unix.sh")
    print("="*60 + "\n")

    return 0 if all_good else 1

if __name__ == "__main__":
    sys.exit(main())
