from fpdf import FPDF

# Create a custom class to include footer
class PDFWithFooter(FPDF):
    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(128)
        self.cell(0, 10, "Sunshine Elementary: Miss Clines' Classroom", 0, 0, "C")

# Create instance of PDF
pdf = PDFWithFooter()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Title
pdf.set_font("Arial", "B", 16)
pdf.cell(0, 10, "Florida Weather Impacts Worksheet", ln=True, align="C")
pdf.ln(10)

# Name and Date fields
pdf.set_font("Arial", "", 12)
pdf.cell(0, 10, "Name: _______________________", ln=True)
pdf.cell(0, 10, "Date: ________________________", ln=True)
pdf.ln(5)

# Directions
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Directions:", ln=True)
pdf.set_font("Arial", "", 12)
directions = ("Florida has many types of weather. Choose one of the weather types below. Then:\n"
              "1. Draw a picture of how this weather affects people, animals, or the land in Florida.\n"
              "2. Write 2-3 sentences to explain what your picture shows and how this weather impacts life in Florida.")
pdf.multi_cell(0, 8, directions)
pdf.ln(5)

# Weather types
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Choose one:", ln=True)
pdf.set_font("Arial", "", 12)
weather_types = "Mild Climate    Thunderstorms    Hurricanes    Drought"
pdf.cell(0, 10, weather_types, ln=True)
pdf.ln(5)

# Drawing box
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "My Drawing:", ln=True)
pdf.rect(x=10, y=pdf.get_y(), w=190, h=60)
pdf.ln(65)

# Writing section
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "My Explanation:", ln=True)
pdf.set_font("Arial", "", 12)
for _ in range(4):
    pdf.cell(0, 10, "___________________________________________________________", ln=True)
pdf.ln(5)

# Bonus question
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Bonus Question (optional):", ln=True)
pdf.set_font("Arial", "", 12)
pdf.multi_cell(0, 8, "Would you rather live in a place with cold snowy winters or Florida\'s mild winters? Why?")
for _ in range(2):
    pdf.cell(0, 10, "___________________________________________________________", ln=True)

# Save the PDF
pdf.output("Florida_Weather_Impacts_Worksheet.pdf")
