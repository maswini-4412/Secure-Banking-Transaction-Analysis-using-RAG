from dotenv import load_dotenv

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import CSVLoader
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Load system prompt
with open("prompts/system_prompt.txt", "r", encoding="utf-8") as f:
    system_prompt = f.read()

# Load CSV
loader = CSVLoader("data/bank_transactions.csv")
documents = loader.load()

# Split text
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = splitter.split_documents(documents)

# Embeddings
embeddings = OpenAIEmbeddings()

# Vector store
vectorstore = Chroma.from_documents(
    docs,
    embedding=embeddings,
    persist_directory="chroma_db"
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# Prompt template
prompt = PromptTemplate(
    input_variables=["context", "question"],
    template=f"""
{system_prompt}

Context:
{{context}}

User Question:
{{question}}

Answer:
"""
)

# LLM
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0
)

# Secure RAG function
def ask_secure_rag(question: str):
    docs = retriever.invoke(question)
    context = "\n".join(d.page_content for d in docs)

    final_prompt = prompt.format(
        context=context,
        question=question
    )

    response = llm.invoke(final_prompt)
    return response.content


# CLI loop
while True:
    q = input("\nAsk a question (type 'exit'): ")
    if q.lower() == "exit":
        break

    print("\nAnswer:\n", ask_secure_rag(q))

print(documents[0].page_content)
