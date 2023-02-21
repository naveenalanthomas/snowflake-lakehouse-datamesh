from PyPDF2 import PdfReader 
import _snowflake 
import io 

def pdfextract(file_path): 
    text = '' 
    file = io.BytesIO(_snowflake.open(file_path, is_owner_file=True).read()) 
    reader = PdfReader(file, strict=False) 
    for page in reader.pages: 
        text += page.extract_text() + "\n" 
    return text