import pandas as pd
from langchain_core.documents import Document

def create_documents(df):
    documents = []
    for idx, row in df.iterrows():
        values = [str(v) if pd.notna(v) else "N/A" for v in row.values]
        content = " | ".join(values)
        documents.append(Document(page_content=content, metadata={"row_id": idx}))
    print(f"📚 Created {len(documents)} documents")
    return documents
