from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet

doc = SimpleDocTemplate(
    "energy_report.pdf"
)

styles = getSampleStyleSheet()

content = []

content.append(
    Paragraph(
        "Smart Home Energy Monitoring Report",
        styles['Title']
    )
)

content.append(
    Paragraph(
        "Generated from IoT Monitoring System",
        styles['Normal']
    )
)

doc.build(content)

print("Report Generated")