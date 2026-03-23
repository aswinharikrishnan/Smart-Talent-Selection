import pdfplumber

def extract_text_from_pdf(file_path):
    """
    Advanced PDF extraction that iterates through all pages 
    and uses layout-preservation logic.
    """
    full_content = []
    
    with pdfplumber.open(file_path) as pdf:
        # Fulfills requirement: Handling chaotic variety of designs
        for i, page in enumerate(pdf.pages):
            # layout=True helps maintain the visual structure of columns
            page_text = page.extract_text(layout=True, x_tolerance=2)
            
            if page_text:
                full_content.append(f"--- Page {i+1} ---\n{page_text}")
            else:
                # Fallback if standard extraction fails on a specific page
                words = page.extract_words()
                words.sort(key=lambda x: (x['top'], x['x0']))
                fallback_text = " ".join([w['text'] for w in words])
                full_content.append(f"--- Page {i+1} (Fallback) ---\n{fallback_text}")
                
    return "\n\n".join(full_content)