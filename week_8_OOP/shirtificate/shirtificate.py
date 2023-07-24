from fpdf import FPDF


pdf = FPDF()
pdf.add_page(orientation="portrait", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

pdf.set_font("helvetica", "B", size=40)
pdf.cell(txt="CS50 Shirtificate", center=True, new_y="Next", new_x="left")

pdf.image("shirtificate.png", x=0, y=50)

name = input("Name: ")
with pdf.local_context(text_mode="FILL"):
    pdf.set_font("helvetica", size=30)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(txt=f"{name} took CS50", h=200, center=True)

pdf.output("shirtificate.pdf")
