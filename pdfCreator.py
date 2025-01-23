import streamlit as st
from fpdf import FPDF

# Function to create the PDF
def create_claim_denial_pdf(patient_name, patient_address, patient_city_state_zip, claim_details):
    class ClaimDenialPDF(FPDF):
        def header(self):
            self.set_font("Arial", "B", 12)
            self.cell(0, 10, "Claim Denial Letter", 0, 1, "C")
            self.ln(10)

        def footer(self):
            self.set_y(-15)
            self.set_font("Arial", "I", 8)
            self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")

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

    # Save PDF to a BytesIO object
    pdf_output = BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)
    return pdf_output

# Streamlit App UI
st.title("Claim Denial Letter Generator")
st.write("Fill in the details below to generate a claim denial letter.")

# Input fields for Patient Information
patient_name = st.text_input("Patient Name", "John Doe")
patient_address = st.text_input("Patient Address", "1234 Elm Street, Apt 567")
patient_city_state_zip = st.text_input("City, State, ZIP", "Springfield, IL 62704")

# Input for Claim Details
st.write("### Enter Claim Details")
claim_details = []
num_claims = st.number_input("Number of Claims", min_value=1, step=1, value=3)
for i in range(num_claims):
    st.write(f"#### Claim {i + 1}")
    claim_number = st.text_input(f"Claim Number {i + 1}", key=f"claim_number_{i}")
    service = st.text_input(f"Service {i + 1}", key=f"service_{i}")
    amount_billed = st.text_input(f"Amount Billed {i + 1}", key=f"amount_billed_{i}")
    amount_allowed = st.text_input(f"Amount Allowed {i + 1}", key=f"amount_allowed_{i}")
    insurance_paid = st.text_input(f"Insurance Paid {i + 1}", key=f"insurance_paid_{i}")
    patient_responsibility = st.text_input(f"Patient Responsibility {i + 1}", key=f"patient_responsibility_{i}")

    if claim_number and service:
        claim_details.append({
            "Claim Number": claim_number,
            "Service": service,
            "Amount Billed": amount_billed,
            "Amount Allowed": amount_allowed,
            "Insurance Paid": insurance_paid,
            "Patient Responsibility": patient_responsibility
        })

# Generate PDF Button
if st.button("Generate PDF"):
    if patient_name and patient_address and patient_city_state_zip and claim_details:
        pdf_file = create_claim_denial_pdf(patient_name, patient_address, patient_city_state_zip, claim_details)
        st.success("PDF generated successfully!")
        st.download_button("Download PDF", pdf_file, "Claim_Denial_Letter.pdf", "application/pdf")
    else:
        st.error("Please fill in all required fields.")
