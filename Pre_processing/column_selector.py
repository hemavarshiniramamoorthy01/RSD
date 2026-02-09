# column_selector.py

def keep_metadata_and_content(df):
    """
    Keeps only metadata columns and 'content'
    """
    required_columns = [
        "id",
        "assigned user",
        "reuses",
        "reuses by",
        "verifies by",
        "project name",
        "content"
    ]

    existing_columns = [col for col in required_columns if col in df.columns]
    return df[existing_columns]
