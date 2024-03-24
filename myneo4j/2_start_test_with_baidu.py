from dotenv import load_dotenv
from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from langchain_community.llms.baidu_qianfan_endpoint import QianfanLLMEndpoint
from langchain_openai import OpenAI

load_dotenv()

graph = Neo4jGraph(
    url="bolt://localhost:7687",
    username="neo4j",
    password="x"
)

llm = QianfanLLMEndpoint(
    model="ChatGLM3-6B"
)

print(llm('Tell me your model name'))

chain = GraphCypherQAChain.from_llm(
    llm, graph=graph, verbose=True,
)

chain.run("""
How many entities exist?
""")

# neo4j plugin issue
# https://github.com/langchain-ai/langchain/issues/12901

# ref
# https://blog.csdn.net/zeroheitao/article/details/122925845?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522171118325316800185852379%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=171118325316800185852379&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-122925845-null-null.142^v99^pc_search_result_base4&utm_term=neo4j&spm=1018.2226.3001.4187
# https://bratanic-tomaz.medium.com/constructing-knowledge-graphs-from-text-using-openai-functions-096a6d010c17
# https://medium.com/neo4j/langchain-cypher-search-tips-tricks-f7c9e9abca4d
