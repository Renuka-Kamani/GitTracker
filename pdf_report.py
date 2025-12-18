from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from datetime import datetime
from config import REPORT_DIR

def generate_pdf(student_info):
    """Create PDF report with GitHub data."""
    username = student_info["username"]
    filename = REPORT_DIR / f"{username}_report.pdf"

    c = canvas.Canvas(str(filename), pagesize=A4)
    width, height = A4
    margin = 20 * mm
    y = height - margin

    c.setFont("Helvetica-Bold", 16)
    c.drawString(margin, y, f"GitHub Activity Report")
    y -= 20

    c.setFont("Helvetica", 12)
    c.drawString(margin, y, f"Username: {student_info['username']}")
    y -= 15
    c.drawString(margin, y, f"Total Repositories: {student_info['total_repos']}")
    y -= 15
    c.drawString(margin, y, f"Total Commits: {student_info['total_commits']}")
    y -= 15
    c.drawString(margin, y, f"Last Commit Date: {student_info['last_commit']}")
    y -= 25

    c.setFont("Helvetica", 9)
    c.drawString(margin, y, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    c.save()
    print(f"✅ PDF report generated: {filename}")
