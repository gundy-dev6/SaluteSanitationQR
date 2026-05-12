# Salute Sanitation QR Generator

This project generates printable SVG labels with:
- A QR code containing a unique latrine ID
- A title line (default: "Salute to Service")
- The same unique ID printed below the QR code

The script currently generates 100 files by default, named like:
- `LATRINE-00001.svg`
- `LATRINE-00002.svg`
- ...

## Project Structure

- `src/generate_latrine_qr_svgs.py` - Main source script
- `run_generate_qr.ps1` - Simple PowerShell runner for this workspace
- `output/latrine_qr_svgs/` - Generated SVG files
- `.venv/` - Local Python virtual environment

## Requirements

- Windows PowerShell
- Python 3.14+ (or compatible)
- Python package: `qrcode[pil]`

## Quick Start (Recommended)

From the project root, run:

```powershell
powershell -ExecutionPolicy Bypass -File .\run_generate_qr.ps1
```

This uses the workspace virtual environment at `.venv` and runs the generator script.

## Manual Run

If you want to run the script directly:

```powershell
.\.venv\Scripts\python.exe .\src\generate_latrine_qr_svgs.py
```

## Configure Output

Edit values in `src/generate_latrine_qr_svgs.py`:
- `PREFIX` - ID prefix (default: `LATRINE`)
- `START_NUMBER` - First sequence number
- `TOTAL_IMAGES` - Number of labels to generate
- `TITLE_TEXT` - Header text shown above QR
- `SVG_WIDTH` / `SVG_HEIGHT` - Label canvas size
- `QR_SIZE`, `QR_X`, `QR_Y` - QR placement and size
- `ID_TEXT_GAP`, `ID_FONT_SIZE` - ID text spacing and style

Output is always written to:

```text
output/latrine_qr_svgs/
```

## Expected Result

After running, the console prints:

```text
Generated 100 SVG files in folder: <project>\output\latrine_qr_svgs
```

You can then print or distribute files from `output/latrine_qr_svgs/`.

## Troubleshooting

### ModuleNotFoundError: No module named qrcode
Install dependency into the workspace venv:

```powershell
.\.venv\Scripts\python.exe -m pip install qrcode[pil]
```

### Python venv not found
If `run_generate_qr.ps1` reports missing venv, create one and install dependency:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install qrcode[pil]
```
