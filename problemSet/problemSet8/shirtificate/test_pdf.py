from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=12)
pdf.cell(0, 10, "Hello World!", ln=1)
pdf.output("test.pdf")
