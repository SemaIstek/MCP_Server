from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate

llm = Ollama(model="llama3.2:1b")

prompt = PromptTemplate(
    input_variables=["context", "question"],
    template="""
You are an assistant that answers questions using ONLY the CSV data.

CSV DATA:
{context}

Question:
{question}

If the answer is not in the CSV, say:
"I cannot find this information in the CSV."
"""
)

def ask(vectorstore, question: str):
    docs = vectorstore.similarity_search(question, k=5)
    context = "\n".join(d.page_content for d in docs)
    return llm.invoke(prompt.format(context=context, question=question))
