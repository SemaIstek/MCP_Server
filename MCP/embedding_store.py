from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

def create_faiss(documents):
    embeddings = OllamaEmbeddings(model="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(
        texts=[doc.page_content for doc in documents],
        embedding=embeddings,
        metadatas=[doc.metadata for doc in documents]
    )
    print("✅ Vector store created successfully")
    return vectorstore
