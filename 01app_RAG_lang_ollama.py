## ollama RAG(URLs) by langchain-ChatOllama

from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_community import embeddings
from langchain_community.chat_models import ChatOllama
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain.text_splitter import CharacterTextSplitter

model_local = ChatOllama(model="mistral:v0.2")

# 1. 데이터를 청크 단위로 분할하기

## Type. url 
# urls = [
#     'https://ko.wikipedia.org/wiki/%EB%8D%A9%EC%9D%B4%EC%A7%93%EA%B8%B0',
#     'https://clearfluency.co.kr/28/?q=YToyOntzOjEyOiJrZXl3b3JkX3R5cGUiO3M6MzoiYWxsIjtzOjQ6InBhZ2UiO2k6MTt9&bmode=view&idx=8534389&t=board'
# ]
# docs = [WebBaseLoader(url).load() for url in urls]
# docs_list = [item for sublist in docs for item in sublist]
# text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size=7500, chunk_overlap=100)
# doc_splits = text_splitter.split_documents(docs_list)

## Type. pdf
# loader = PyPDFLoader("청킹.pdf")
# doc_splits = loader.load_and_split()

## Type. txt
with open('청킹.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    
from langchain.docstore.document import Document
chunks = []
chunk_size = 35 # Characters
for i in range(0, len(text), chunk_size):
    chunk = text[i:i + chunk_size]
    chunks.append(chunk)
documents = [Document(page_content=chunk, metadata={"source": "local"}) for chunk in chunks]
    
    
    
# 2. 문서를 임베딩으로 변환하여 저장하기
vectorstore = Chroma.from_documents(
    documents=documents,
    collection_name="rag-chroma",
    embedding=embeddings.ollama.OllamaEmbeddings(model='nomic-embed-text'),
)
retriever = vectorstore.as_retriever()


# 3. RAG 이전 버전
print("Before RAG\n")
before_rag_template = "What is {topic}"
before_rag_prompt = ChatPromptTemplate.from_template(before_rag_template)
before_rag_chain = before_rag_prompt | model_local | StrOutputParser()
print(before_rag_chain.invoke({"topic": "청킹(Chunking)"}))


# 4. RAG 적용 이후
print("\n########\nAfter RAG\n")
after_rag_template = """
Answer the question based only on the following context:
{context}
Question: {question}
"""
after_rag_prompt = ChatPromptTemplate.from_template(after_rag_template)
after_rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | after_rag_prompt
    | model_local
    | StrOutputParser()
)
print(after_rag_chain.invoke("청킹(Chunking)이 무슨 뜻이야?"))

