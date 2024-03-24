from dotenv import load_dotenv
from langchain.chains import GraphCypherQAChain
from langchain.chat_models import ChatOpenAI
from langchain.graphs import Neo4jGraph

load_dotenv()

graph = Neo4jGraph(
    url="xx://localhost:7687",
    username="neo4j",
    password="xx"
)

chain = GraphCypherQAChain.from_llm(
    ChatOpenAI(temperature=0), graph=graph, verbose=True,
)

chain.run("""
How many entities exist?
""")

# neo4j plugin issue
# https://github.com/langchain-ai/langchain/issues/12901