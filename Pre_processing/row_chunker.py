def row_based_chunking(df):
    """
    Each row = one chunk
    """
    chunks = []

    metadata_columns = [col for col in df.columns if col not in ["id", "content"]]

    for _, row in df.iterrows():
        chunks.append({
            "text": row["content"],
            "metadata": {
                "chunk_id": row["id"],
                **{col: row[col] for col in metadata_columns}
            }
        })

    return chunks
