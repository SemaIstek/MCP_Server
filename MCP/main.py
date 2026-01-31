from load_data import load_csv
from preprocess import create_documents
from embedding_store import create_chroma, load_chroma
from rag_query import ask
import os
import logging

def main():
    df = load_csv("../assets/filtered_data.csv")
    documents = create_documents(df)
    
    # Check if Chroma database already exists
    chroma_path = "./vector_db/chroma_db"
    if os.path.exists(chroma_path):
        logging.info("📂 Loading existing Chroma database...")
        vectorstore = load_chroma()
    else:
        logging.info("🆕 Creating new Chroma database...")
        vectorstore = create_chroma(documents)
    
    # test question
    answer = ask(vectorstore, "Summarize this dataset")
    logging.info("Answer:\n%s", answer)
   

if __name__ == "__main__":
    main()
