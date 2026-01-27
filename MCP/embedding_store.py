import os
from pathlib import Path
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Create vector_db directory
vector_db_dir = "./vector_db"
Path(vector_db_dir).mkdir(exist_ok=True)

def create_chroma(documents):
    """Create and persist Chroma vector store"""
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    chroma_path = os.path.join(vector_db_dir, "chroma_db")
    
    vectorstore = Chroma.from_texts(
        texts=[doc.page_content for doc in documents],
        embedding=embeddings,
        metadatas=[doc.metadata for doc in documents],
        persist_directory=chroma_path
    )
    print(f"✅ Chroma Vector store created and persisted at: {chroma_path}")
    return vectorstore

def load_chroma():
    """Load existing Chroma vector store from disk"""
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    chroma_path = os.path.join(vector_db_dir, "chroma_db")
    
    if os.path.exists(chroma_path):
        vectorstore = Chroma(
            embedding_function=embeddings,
            persist_directory=chroma_path
        )
        print(f"✅ Chroma Vector store loaded from: {chroma_path}")
        return vectorstore
    else:
        print(f"❌ Chroma database not found at: {chroma_path}")
        return None
