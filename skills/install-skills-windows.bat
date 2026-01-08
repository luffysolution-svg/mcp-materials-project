@echo off
REM Materials Project Skills - Correct Installation for Claude Code
REM Installs skills in SKILL.md format (the correct way)

echo ========================================
echo Materials Project Skills Installer
echo Claude Code SKILL.md Format
echo ========================================
echo.

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not installed
    pause
    exit /b 1
)

echo [1/6] Python version:
python --version
echo.

REM Check API Key
if "%MP_API_KEY%"=="" (
    echo [WARNING] MP_API_KEY not set
    echo Get your key from https://materialsproject.org/api
    echo Run: setx MP_API_KEY "your_key_here"
    echo.
    set /p CONTINUE="Continue anyway? (y/n): "
    if /i not "%CONTINUE%"=="y" exit /b 1
)

REM Install dependencies
echo [2/6] Installing dependencies...
pip install mp-api pandas openpyxl
echo.

REM Create skill directories
echo [3/6] Creating skill directories...
set SKILLS_DIR=%USERPROFILE%\.claude\skills
mkdir "%SKILLS_DIR%\materials-search" 2>nul
mkdir "%SKILLS_DIR%\materials-export" 2>nul
mkdir "%SKILLS_DIR%\materials-compare" 2>nul
echo Created skill directories
echo.

REM Copy SKILL.md files
echo [4/6] Copying SKILL.md files...
copy /Y "skills\skill-definitions\materials-search.SKILL.md" "%SKILLS_DIR%\materials-search\SKILL.md" >nul
copy /Y "skills\skill-definitions\materials-export.SKILL.md" "%SKILLS_DIR%\materials-export\SKILL.md" >nul
copy /Y "skills\skill-definitions\materials-compare.SKILL.md" "%SKILLS_DIR%\materials-compare\SKILL.md" >nul
echo Copied 3 SKILL.md files
echo.

REM Copy Python scripts
echo [5/6] Copying Python scripts...
copy /Y "skills\scripts\materials_search.py" "%SKILLS_DIR%\materials-search\" >nul
copy /Y "skills\scripts\materials_export.py" "%SKILLS_DIR%\materials-export\" >nul
copy /Y "skills\scripts\materials_compare.py" "%SKILLS_DIR%\materials-compare\" >nul
echo Copied 3 Python scripts
echo.

REM Test
echo [6/6] Testing installation...
python "%SKILLS_DIR%\materials-search\materials_search.py" --help >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Test failed
    pause
    exit /b 1
)

echo.
echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo Skills installed at:
echo   %SKILLS_DIR%\materials-search\
echo   %SKILLS_DIR%\materials-export\
echo   %SKILLS_DIR%\materials-compare\
echo.
echo Each directory contains:
echo   - SKILL.md (skill definition)
echo   - Python script
echo.
echo Available skills:
echo   /materials-search  - Search materials database
echo   /materials-export  - Export to Excel
echo   /materials-compare - Compare materials
echo.
echo IMPORTANT: Restart Claude Code to load skills!
echo.
echo Usage:
echo   /materials-search --formula Si
echo   /materials-export --material-id mp-149 --output silicon.xlsx
echo   /materials-compare mp-149 mp-2534
echo.
pause
