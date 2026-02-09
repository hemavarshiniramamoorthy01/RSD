# content_merger.py

def merge_columns_to_content(df):
    """
    Merges all non-metadata columns into 'content'
    """
    exclude_columns = {
        "id",
        "assigned user",
        "reuses",
        "reuses by",
        "verifies by",
        "project name"
    }

    content_columns = [
        col for col in df.columns
        if col.lower() not in exclude_columns
    ]

    df["content"] = (
        df[content_columns]
        .astype(str)
        .fillna("")
        .agg(" ".join, axis=1)
    )

    return df
