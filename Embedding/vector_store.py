# from langchain_community.vectorstores import Chroma

# def store_documents(documents, embeddings, persist_dir="chroma_store"):
#     db = Chroma.from_documents(
#         documents=documents,
#         embedding=embeddings,
#         persist_directory=persist_dir
#     )
#     db.persist()
#     return db
import os
from langchain_chroma import Chroma

def store_documents(documents, embeddings, persist_dir="chroma_store"):
    persist_dir = os.path.abspath(persist_dir)
    print(f"   → Persist directory: {persist_dir}")

    os.makedirs(persist_dir, exist_ok=True)

    print("   → Creating Chroma vector store (no auto-persist)")
    db = Chroma(
        embedding_function=embeddings,
        persist_directory=persist_dir
    )

    print("   → Adding documents to Chroma")
    db.add_documents(documents)

    print("   → Persisting ChromaDB to disk")
    db.persist()

    print("   → Chroma.from_documents finished successfully")
    return db

