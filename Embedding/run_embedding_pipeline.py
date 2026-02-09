from Pre_processing.main import preprocess_excel
from Embedding.embedding_model import load_embedding_model
from Embedding.document_builder import chunks_to_documents
from Embedding.vector_store import store_documents


def build_vector_db(excel_path):
    print("STEP 1: Preprocessing + chunking started")
    chunks = preprocess_excel(excel_path)
    print(f"STEP 1 DONE: {len(chunks)} chunks created")

    print("STEP 2: Converting chunks to Documents")
    documents = chunks_to_documents(chunks)
    print(f"STEP 2 DONE: {len(documents)} documents created")

    print("STEP 3: Loading embedding model")
    embeddings = load_embedding_model()
    print("STEP 3 DONE: Embedding model loaded")

    print("STEP 4: Storing documents in ChromaDB")
    db = store_documents(documents, embeddings)
    print("STEP 4 DONE: ChromaDB created")

    return db


if __name__ == "__main__":
    print("PIPELINE STARTED")
    db = build_vector_db(r"C:\Users\hp\Desktop\PJT\Example.xlsx")
    print("PIPELINE FINISHED SUCCESSFULLY")
