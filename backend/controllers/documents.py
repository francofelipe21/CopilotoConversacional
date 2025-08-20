from PyPDF2 import PdfReader, PdfWriter
from agent.load import insert_new_document

async def new_pdfs(files):
    for file in files:
        reader = PdfReader(file.file)
        writer = PdfWriter()
        for page in reader.pages:
            writer.add_page(page)
        path_file = "uploaded_pdfs/"+str(file.filename)
        with open(path_file, 'wb') as exit_file:
            writer.write(exit_file)
        response = await insert_new_document(file.filename)
        if response["status_code"] != 200:
            return response["status_code"]
    return {"status_code" : 200}