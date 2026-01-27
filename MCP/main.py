from load_data import load_csv
from preprocess import create_documents
from embedding_store import create_chroma, load_chroma
from rag_query import ask
import os

def main():
    df = load_csv("../assets/filtered_data.csv")
    documents = create_documents(df)
    
    # Check if Chroma database already exists
    chroma_path = "./vector_db/chroma_db"
    if os.path.exists(chroma_path):
        print("📂 Loading existing Chroma database...")
        vectorstore = load_chroma()
    else:
        print("🆕 Creating new Chroma database...")
        vectorstore = create_chroma(documents)
    
    # test question
    answer = ask(vectorstore, "Summarize this dataset")
    print(f"Answer:\n{answer}")
   

if __name__ == "__main__":
    main()
