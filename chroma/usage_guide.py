import chromadb

# chroma中自定义Embeddings的几种方法
# https://zhuanlan.zhihu.com/p/649413704

# onnx.tar.gz
# https://developer.aliyun.com/article/1464026
# https://chroma-onnx-models.s3.amazonaws.com/all-MiniLM-L6-v2/onnx.tar.gz

# python can also run in-memory with no server running: chromadb.PersistentClient()
client = chromadb.PersistentClient()
collection = client.get_or_create_collection(name="my_collection")
col_cnt = collection.count()
print(f"Collection count: {col_cnt}")

collection.add(
    documents=["lorem ipsum...", "doc2", "doc3"],
    metadatas=[{"chapter": "3", "verse": "16"}, {"chapter": "3", "verse": "5"}, {"chapter": "29", "verse": "11"}],
    ids=["id1", "id2", "id3"]
)
col_cnt = collection.count()
print(f"Collection count: {col_cnt}")

