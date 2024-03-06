# corpus_processor.py

def count_token_occurrences(file_path, token):
    with open(file_path, 'r') as file:
        corpus_text = file.read()
        # Case-insensitive count
        count = corpus_text.lower().count(token.lower())
    return count
