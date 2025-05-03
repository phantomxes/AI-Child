from fpdf import FPDF
from pathlib import Path
import json
from datetime import datetime

memory_path = Path.home() / "1man.army" / "memory" / "experience_log.json"
output_dir = Path.home() / "1man.army" / "intel"
output_dir.mkdir(parents=True, exist_ok=True)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="1man.army Scan Report", ln=True, align="C")
pdf.ln(10)

with open(memory_path, 'r') as f:
    data = json.load(f)

for entry in data[-5:]:
    pdf.cell(200, 10, txt=f"{entry['timestamp']} | {entry['label']}", ln=True)
    pdf.multi_cell(0, 10, entry['output_snippet'])

filename = output_dir / f"scan_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
pdf.output(str(filename))
print(f"[📥] Report saved to {filename}")
