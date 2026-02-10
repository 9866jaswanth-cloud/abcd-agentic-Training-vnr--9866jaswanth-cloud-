import re
def tokenizer(text):
    # convert to lowercase
    text = text.lower()
    # remove punctuation
    text = re.sub(r'[^a-z0-9\s]', '', text)
    # split into tokens
    tokens = text.split()
    return tokens
# Example
sentence = "Hello, world! NLP is fun."
print(tokenizer(sentence))


import re
def tokenizer(text):
    tokens = re.findall(r'\b\w+\b', text.lower())
    return tokens

print(tokenizer("AI costs $100 in 2025!"))
