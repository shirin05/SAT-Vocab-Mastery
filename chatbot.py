import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet

def get_synonyms(word):
    synonyms = []       
    for synset in wordnet.synsets(word):
        for lemma in synset.lemmas():
            # if synonyms had two words, it gave _ between, here we fix that issue
            synonym = lemma.name().replace('_',' ')
            # append modified synonym to list
            # dont do append(lemma.name()) as that is the original unmodified synonym
            synonyms.append(synonym)
    return list(set(synonyms)) 



