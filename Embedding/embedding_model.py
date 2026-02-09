import os
os.environ["TRANSFORMERS_NO_TF"] = "1"

from langchain_huggingface import HuggingFaceEmbeddings


def load_embedding_model():
    print("  → Initializing HuggingFaceEmbeddings (sentence BASE)")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={"device": "cpu"},
        encode_kwargs={"normalize_embeddings": True}
    )
    print("  → HuggingFaceEmbeddings initialized successfully")
    return embeddings
