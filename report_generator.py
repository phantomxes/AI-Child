from fpdf import FPDF
import json
from pathlib import Path
from datetime import datetime

# 📁 File locations
MEMORY_FILE = Path.home() / "1man.army" / "memory" / "experience_log.json"
OUTPUT_DIR = Path.home() / "1man.army" / "intel"
OUTPUT_DIR.mkdir(exist_ok=True)

report_file = OUTPUT_DIR / f"scan_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"

# 📄 Setup PDF doc
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.set_title("Scan Report - 1man.army")
pdf.set_author("1manarmy AI")

# 📥 Load memory
with open(MEMORY_FILE, 'r') as f:
    data = json.load(f)

# 📊 Include last few logs
pdf.cell(200, 10, txt="1man.army – Scan Intel Report", ln=True, align="C")
pdf.ln(10)

for entry in data[-5:]:  # Last 5 scans
    pdf.set_font("Arial", size=11)
    pdf.cell(200, 10, txt=f"Scan: {entry['timestamp']} | Tool: {entry['label']}", ln=True)
    pdf.multi_cell(0, 10, txt=entry["output_snippet"][:1000])
    pdf.ln(5)

# 💾 Save
pdf.output(str(report_file))
print(f"[✓] Report generated: {report_file}")
