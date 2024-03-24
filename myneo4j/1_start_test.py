from dotenv import load_dotenv
from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from langchain_openai import OpenAI

load_dotenv()

graph = Neo4jGraph(
    url="bolt://localhost:7687",
    username="neo4j",
    password="x"
)

llm = OpenAI()

chain = GraphCypherQAChain.from_llm(
    llm, graph=graph, verbose=True,
)

chain.run("""
How many entities exist?
""")

# neo4j plugin issue
# https://github.com/langchain-ai/langchain/issues/12901