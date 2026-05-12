from pathlib import Path
import qrcode

# -----------------------------
# Configuration
# -----------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_FOLDER = PROJECT_ROOT / "output" / "latrine_qr_svgs"

PREFIX = "LATRINE"
START_NUMBER = 1
TOTAL_IMAGES = 100

SVG_WIDTH = 600
SVG_HEIGHT = 800

TITLE_TEXT = "Salute to Service"
TITLE_FONT_SIZE = 48
ID_FONT_SIZE = 42

TITLE_Y = 100

# QR layout
QR_SIZE = 420
QR_X = (SVG_WIDTH - QR_SIZE) / 2
QR_Y = 135  # tightened spacing below title

# ID text layout
ID_TEXT_GAP = 55
ID_TEXT_Y = QR_Y + QR_SIZE + ID_TEXT_GAP

# QR settings
QR_BORDER = 4
ERROR_CORRECTION = qrcode.constants.ERROR_CORRECT_H

# -----------------------------
# Create output folder
# -----------------------------
OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Generate one SVG
# -----------------------------
def generate_qr_svg(unique_id: str, output_path: Path):
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECTION,
        border=QR_BORDER,
    )

    qr.add_data(unique_id)
    qr.make(fit=True)

    matrix = qr.get_matrix()
    module_count = len(matrix)
    module_size = QR_SIZE / module_count

    qr_rects = []

    for row_index, row in enumerate(matrix):
        for col_index, is_dark in enumerate(row):
            if is_dark:
                x = QR_X + (col_index * module_size)
                y = QR_Y + (row_index * module_size)
                qr_rects.append(
                    f'<rect x="{x:.3f}" y="{y:.3f}" width="{module_size:.3f}" height="{module_size:.3f}" fill="black"/>'
                )

    qr_svg_rects = "\n    ".join(qr_rects)

    label_svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg width="{SVG_WIDTH}" height="{SVG_HEIGHT}" viewBox="0 0 {SVG_WIDTH} {SVG_HEIGHT}"
xmlns="http://www.w3.org/2000/svg">

<rect width="100%" height="100%" fill="white"/>

<text x="50%" y="{TITLE_Y}"
text-anchor="middle"
font-family="Arial, Helvetica, sans-serif"
font-size="{TITLE_FONT_SIZE}"
font-weight="700"
fill="black">
{TITLE_TEXT}
</text>

<g id="qr-code">
    {qr_svg_rects}
</g>

<text x="50%" y="{ID_TEXT_Y}"
text-anchor="middle"
font-family="Arial, Helvetica, sans-serif"
font-size="{ID_FONT_SIZE}"
font-weight="700"
letter-spacing="2"
fill="black">
{unique_id}
</text>

</svg>
"""

    with open(output_path, "w", encoding="utf-8") as file:
        file.write(label_svg)

# -----------------------------
# Generate 100 SVG files
# -----------------------------
for i in range(START_NUMBER, START_NUMBER + TOTAL_IMAGES):
    unique_id = f"{PREFIX}-{i:05d}"
    filename = f"{unique_id}.svg"
    output_path = OUTPUT_FOLDER / filename

    generate_qr_svg(unique_id, output_path)

print(f"Generated {TOTAL_IMAGES} SVG files in folder: {OUTPUT_FOLDER}")
