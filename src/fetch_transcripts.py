from langchain.document_loaders import PyPDFLoader

def load_transcript(path):
    return PyPDFLoader(path).load()
# Functions for loading corporate transcripts using LangChain
