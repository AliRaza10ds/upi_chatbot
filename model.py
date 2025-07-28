from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
openai_api_key=os.getenv("OPENAI_API_KEY")

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","you are a helpful UPI assistant"),
        ("user","each new step should start from new line.{input}")
    ]
)
llm=ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    openai_api_key=openai_api_key
)
parser=StrOutputParser()

chain=prompt|llm|parser

def get_bot_response(user_input):
    return chain.invoke({"input":user_input})