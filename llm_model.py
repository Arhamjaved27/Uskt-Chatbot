from langchain.vectorstores import FAISS
from langchain.llms import GooglePalm
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import os

from dotenv import load_dotenv


load_dotenv()  # take environment variables from .env (especially openai api key)

# Create Google Palm LLM model
llm = GooglePalm(google_api_key=os.environ["GOOGLE_API_KEY"], temperature=0.1)
# # Initialize instructor embeddings using the Hugging Face model
instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")
vectordb_file_path = "vector_DB"

def create_vector_db():
    # Load data from FAQ sheet
    loader = CSVLoader(file_path='intents.csv', source_column="prompt")
    data = loader.load()

    # Create a FAISS instance for vector database from 'data'
    vectordb = FAISS.from_documents(documents=data,
                                    embedding=instructor_embeddings)

    # Save vector database locally
    vectordb.save_local(vectordb_file_path)

def get_qa_chain():
    # Load the vector database from the local folder
    vectordb = FAISS.load_local(vectordb_file_path, instructor_embeddings)

    # Create a retriever for querying the vector database
    retriever = vectordb.as_retriever(score_threshold=5)

    prompt_template = """You are a university guide chatbot. Your role is to provide accurate and helpful information about
      the university.Given the following context and a question,
      You must only generate responses based on this context provided to you.
      In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
      If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer by yourself.
    
      
      Always maintain a friendly and professional tone.
      
      CONTEXT: {context}
      QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    chain = RetrievalQA.from_chain_type(llm=llm,
                                        chain_type="stuff",
                                        retriever=retriever,
                                        input_key="query",
                                        return_source_documents=True,
                                        chain_type_kwargs={"prompt": PROMPT})

    
    return chain

if __name__ == "__main__":
    # create_vector_db()
    chain = get_qa_chain()
    # print(chain("Do you have javascript course?"))
    
    

    while(1):
        q = input("Enter Question: ")
        try:
            response = chain({"query": q+"?"})
            print(response["result"])
        except IndexError as e:
            print(f"An error occurred: {e}")
            print("The LLM response was empty or malformed.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")