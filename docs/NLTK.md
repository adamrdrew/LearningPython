# NLTK


# Tokenize
Pretty simple. We do need to make sure we have the `punk` tokenizer installed. 
```python
>>> import nltk
>>> nltk.download('punkt')
[nltk_data] Downloading package punkt to /home/adam/nltk_data...
[nltk_data]   Package punkt is already up-to-date!
True
>>> tokens = nltk.word_tokenize("Hey check out this dope sentence. It is so worth analyzing.")
>>> tokens
['Hey', 'check', 'out', 'this', 'dope', 'sentence', '.', 'It', 'is', 'so', 'worth', 'analyzing', '.']
>>> type(tokens)
<class 'list'>
```

