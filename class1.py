import re


def clue_decrypt(file_path):
    with open(file_path,'r') as file:
        file_content = file.read()
    return file_content

def count_python_keywords(contents):
    python_keywords = ["and", "as", "assert", "break", "class", "continue", "def", "del", "elif", "else", "except",
                       "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "nonlocal", "not",
                       "or", "pass", "raise", "return", "try", "while", "with", "yield"]
    keyword_count = {keyword: 0 for keyword in python_keywords}
    for keyword in python_keywords:
        occurrences = re.findall(r'\b' + re.escape(keyword) + r'\b', contents)
        keyword_count[keyword] = len(occurrences)
        return keyword_count

file_path = 'mysterious.txt'
contents = clue_decrypt(file_path)
keyword_counts = count_python_keywords(contents)

for keyword, count in keyword_counts.items():
    print(f"{keyword}: {count}")