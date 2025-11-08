from fpdf import FPDF

def main():
    name = input("Name: ")
    pdf = FPDF(orientation="p", unit="mm", format="A4")
    pdf.add_page()

    pdf.set_font("helvetica", "B", 40)
    pdf.cell(0, 60, "CS50 Shirtificate", align="C")

    pdf.image("shirtificate.png", x=0, y=60, w=120)

    pdf.set_font("helvetica", "B", 30)
    pdf.set_text_color(255, 255, 255)
    pdf.text(x=30, y=140, txt=f"{name} took CS50")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
