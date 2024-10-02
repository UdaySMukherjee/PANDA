from fpdf import FPDF
import time

# Function to generate a report and save it as a PDF
def generate_report(passage):
    # Create a PDF object
    pdf = FPDF()
    pdf.add_page()
    
    # Set font and add a title
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Conversation Report", ln=True, align='C')
    
    # Add some basic content
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(200, 10, txt="Thank you for using DR.PANDA. Below is a summary of your conversation:", ln=True)
    pdf.ln(10)

    # Add the entire conversation passage
    pdf.multi_cell(0, 10, txt=passage)

    # Save the PDF file
    file_name = "conversation_report.pdf"
    pdf.output(file_name)
    print(f"Report generated and saved as {file_name}")
