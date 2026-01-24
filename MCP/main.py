from load_data import load_csv
from preprocess import create_documents
from embedding_store import create_faiss
from rag_query import ask

def main():
    df = load_csv("../assets/filtered_data.csv")
    documents = create_documents(df)
    vectorstore = create_faiss(documents)
    
    # test question
    answer = ask(vectorstore, "Which country suffered the most damage?")
    print(f"Answer:\n{answer}")

if __name__ == "__main__":
    main()
