import sys
from langchain_community.document_loaders import CSVLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
# from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings


def load_document(filename):
    loader = CSVLoader(filename, autodetect_encoding=True)
    # loader = PyPDFLoader(filename)
    pages = loader.load()
    python_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=400)
    splits = python_splitter.split_documents(pages)
    Chroma.from_documents(
        documents=splits,
        # embedding=OpenAIEmbeddings(model="text-embedding-3-small"),
        embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001"),
        persist_directory="data",
    )


load_document(sys.argv[1])
