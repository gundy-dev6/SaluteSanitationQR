$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$PythonExe = Join-Path $ProjectRoot ".venv\Scripts\python.exe"
$ScriptPath = Join-Path $ProjectRoot "src\generate_latrine_qr_svgs.py"

if (-not (Test-Path $PythonExe)) {
    throw "Python venv not found at $PythonExe"
}

& $PythonExe $ScriptPath
