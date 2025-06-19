import os
from langchain_community.document_loaders import PyPDFLoader

def load_transcript_texts(raw_folder="../data/raw"):
    raw_folder = os.path.abspath(raw_folder)  # ← NEW: ensure it's absolute
    pdf_files = [f for f in os.listdir(raw_folder) if f.endswith(".pdf")]
    docs = []

    for file in pdf_files:
        path = os.path.join(raw_folder, file)
        loader = PyPDFLoader(path)
        pages = loader.load()
        docs.extend(pages)

    return docs

