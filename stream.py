import streamlit as st
import PyPDF2
import re
import webbrowser

def extract_email_from_pdf(pdf_file):
    # Open the PDF file
    pdf = PyPDF2.PdfFileReader(pdf_file)
    
    # Loop through each page of the PDF
    for i in range(pdf.getNumPages()):
        page = pdf.getPage(i)
        text = page.extractText()
        
        # Use a regular expression to find the email address
        match = re.search(r'[\w\.-]+@[\w\.-]+', text)
        if match:
            return match.group(0)
        
    return None

def main():
    st.set_page_config(page_title="PDF Email Extractor App", page_icon=":guardsman:", layout="wide")
    st.title("Upload PDF File")
    file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if file is not None:
        email = extract_email_from_pdf(file)
        if email:
            st.success(f"COR email found: {email}")
            
            # Add a button to create an email to the COR
            if st.button("Create Email"):
                webbrowser.open(f"mailto:{email}")
        else:
            st.error("COR email not found")

if __name__ == '__main__':
    main()
