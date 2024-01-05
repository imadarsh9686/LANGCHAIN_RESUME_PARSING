from typing import List, Optional

from langchain.callbacks import get_openai_callback
from langchain.chat_models import ChatOpenAI

from kor.extraction import create_extraction_chain
from kor.nodes import Object, Text, Number

import pandas as pd
from pydantic import BaseModel, Field, validator
from kor import extract_from_documents, from_pydantic, create_extraction_chain
import os

from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter


from langchain.text_splitter import CharacterTextSplitter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from time import sleep
from typing import Dict, List, Optional, Any
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import TextLoader
from langchain.document_loaders import Docx2txtLoader


def process_file(uploaded_file):

    bytes_data = uploaded_file.read()
    _, file_extension = os.path.splitext(uploaded_file.name)

    # write the uploaded file to disk
    with open(uploaded_file.name, 'wb') as f:
        f.write(bytes_data)

    documents = None
    if file_extension.lower() == '.pdf':

        # Load the PDF file with PyPDF Loader
        loader = PyPDFLoader(uploaded_file.name)
        documents = loader.load()

    elif file_extension == ".docx" or file_extension == ".doc":

        loader = Docx2txtLoader(uploaded_file.name)
        documents = loader.load()
            

    elif file_extension.lower() == '.txt':
        # Load the text file with TextLoader
        loader = TextLoader(uploaded_file.name, encoding='utf8')
        documents = loader.load()

    else:
        raise ValueError(f"Unsupported file type: {file_extension}")

    return documents

file= "D:\assignment\resume"

if len(uploaded_files) > 0:


