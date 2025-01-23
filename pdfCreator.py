from fpdf import FPDF

# Define the details for the claim denial letter
patient_name = "John Doe"
patient_address = "1234 Elm Street, Apt 567"
patient_city_state_zip = "Springfield, IL 62704"

claim_details = [
    {
        "Claim Number": "10001",
        "Service": "Consultation",
        "Amount Billed": "$200.00",
        "Amount Allowed": "$180.00",
        "Insurance Paid": "$150.00",
        "Patient Responsibility": "$30.00"
    },
    {
        "Claim Number": "10002",
        "Service": "X-Ray",
        "Amount Billed": "$250.00",
        "Amount Allowed": "$200.00",
        "Insurance Paid": "$180.00",
        "Patient Responsibility": "$20.00"
    },
    {
        "Claim Number": "10003",
        "Service": "Lab Tests",
        "Amount Billed": "$300.00",
        "Amount Allowed": "$250.00",
        "Insurance Paid": "$200.00",
        "Patient Responsibility": "$50.00"
    }
]

# Create the PDF
class ClaimDenialPDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, "Claim Denial Letter", 0, 1, "C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

# Initialize the PDF
pdf = ClaimDenialPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)

# Add Patient Details
pdf.set_font("Arial", size=12)
pdf.cell(0, 10, f"Patient Name: {patient_name}", ln=True)
pdf.cell(0, 10, f"Address: {patient_address}", ln=True)
pdf.cell(0, 10, f"City, State, ZIP: {patient_city_state_zip}", ln=True)
pdf.ln(10)

# Add Claim Details
pdf.set_font("Arial", "B", 12)
pdf.cell(0, 10, "Claim Details:", ln=True)
pdf.set_font("Arial", size=12)

for claim in claim_details:
    pdf.cell(0, 10, f"Claim Number: {claim['Claim Number']}", ln=True)
    pdf.cell(0, 10, f"Service: {claim['Service']}", ln=True)
    pdf.cell(0, 10, f"Amount Billed: {claim['Amount Billed']}", ln=True)
    pdf.cell(0, 10, f"Amount Allowed: {claim['Amount Allowed']}", ln=True)
    pdf.cell(0, 10, f"Insurance Paid: {claim['Insurance Paid']}", ln=True)
    pdf.cell(0, 10, f"Patient Responsibility: {claim['Patient Responsibility']}", ln=True)
    pdf.ln(5)

# Save the PDF to a file
output_path = "/mnt/data/Claim_Denial_Letter.pdf"
pdf.output(output_path)
output_path
