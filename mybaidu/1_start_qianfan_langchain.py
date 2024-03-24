"""For basic init and call"""
from dotenv import load_dotenv

load_dotenv()
from langchain_community.llms import QianfanLLMEndpoint

llm = QianfanLLMEndpoint(streaming=True)
res = llm("hi")
print(res)
