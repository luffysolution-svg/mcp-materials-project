@echo off
REM Materials Project Skills - Global Installation Script for Windows
REM This script installs the skills globally for all projects

echo ========================================
echo Materials Project Skills Installer
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.10+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/5] Checking Python installation...
python --version
echo.

REM Check if MP_API_KEY is set
if "%MP_API_KEY%"=="" (
    echo [WARNING] MP_API_KEY environment variable is not set
    echo.
    echo Please set your Materials Project API key:
    echo   1. Get your key from https://materialsproject.org/api
    echo   2. Run: setx MP_API_KEY "your_api_key_here"
    echo   3. Restart this script
    echo.
    set /p CONTINUE="Continue anyway? (y/n): "
    if /i not "%CONTINUE%"=="y" exit /b 1
    echo.
)

REM Install dependencies
echo [2/5] Installing Python dependencies...
pip install mp-api pandas openpyxl
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)
echo.

REM Create global directory
echo [3/5] Creating global directory...
set GLOBAL_DIR=%USERPROFILE%\.claude\materials-skills
if not exist "%GLOBAL_DIR%\scripts" mkdir "%GLOBAL_DIR%\scripts"
echo Created: %GLOBAL_DIR%
echo.

REM Copy scripts
echo [4/5] Copying scripts...
copy /Y "skills\scripts\materials_search.py" "%GLOBAL_DIR%\scripts\" >nul
copy /Y "skills\scripts\materials_export.py" "%GLOBAL_DIR%\scripts\" >nul
copy /Y "skills\scripts\materials_compare.py" "%GLOBAL_DIR%\scripts\" >nul
echo Copied 3 scripts to %GLOBAL_DIR%\scripts\
echo.

REM Create global skills.json
echo [5/5] Creating global skills configuration...
(
echo {
echo   "skills": {
echo     "materials-search": {
echo       "name": "Materials Search",
echo       "description": "Search Materials Project database for materials by formula, elements, band gap, and other properties",
echo       "command": "python",
echo       "args": [
echo         "%GLOBAL_DIR:\=\\%\\scripts\\materials_search.py"
echo       ],
echo       "env": {
echo         "MP_API_KEY": "${env:MP_API_KEY}",
echo         "PYTHONPATH": "%GLOBAL_DIR:\=\\%"
echo       },
echo       "category": "materials",
echo       "icon": "search"
echo     },
echo     "materials-export": {
echo       "name": "Materials Export",
echo       "description": "Export materials data to professionally formatted Excel files",
echo       "command": "python",
echo       "args": [
echo         "%GLOBAL_DIR:\=\\%\\scripts\\materials_export.py"
echo       ],
echo       "env": {
echo         "MP_API_KEY": "${env:MP_API_KEY}",
echo         "PYTHONPATH": "%GLOBAL_DIR:\=\\%"
echo       },
echo       "category": "materials",
echo       "icon": "download"
echo     },
echo     "materials-compare": {
echo       "name": "Materials Compare",
echo       "description": "Compare multiple materials side by side with detailed property comparison",
echo       "command": "python",
echo       "args": [
echo         "%GLOBAL_DIR:\=\\%\\scripts\\materials_compare.py"
echo       ],
echo       "env": {
echo         "MP_API_KEY": "${env:MP_API_KEY}",
echo         "PYTHONPATH": "%GLOBAL_DIR:\=\\%"
echo       },
echo       "category": "materials",
echo       "icon": "compare"
echo     }
echo   }
echo }
) > "%USERPROFILE%\.claude\skills.json"

echo Created: %USERPROFILE%\.claude\skills.json
echo.

REM Test installation
echo ========================================
echo Testing installation...
echo ========================================
python "%GLOBAL_DIR%\scripts\materials_search.py" --help >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Installation test failed
    pause
    exit /b 1
)

echo.
echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo Skills installed globally at:
echo   %GLOBAL_DIR%
echo.
echo Configuration file:
echo   %USERPROFILE%\.claude\skills.json
echo.
echo Available skills:
echo   /materials-search  - Search materials database
echo   /materials-export  - Export to Excel
echo   /materials-compare - Compare materials
echo.
echo Usage examples:
echo   /materials-search --formula Si
echo   /materials-export --band-gap-min 1.0 --band-gap-max 3.0 --stable
echo   /materials-compare mp-149 mp-2534
echo.
echo Note: Restart Claude Code to load the new skills
echo.
pause
