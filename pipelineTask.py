
# coding: utf-8

# In[1]:


import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from stat_parser import Parser

# In[2]:


class Article:
    def __init__(self, id, title, content, link):
        self.id = id
        self.title = title
        self.content = content
        self.link = link


# In[3]:


def fetchArticles():
    files = ["xac"]
    articles = {}
    for filename in files:
        with open(filename) as data_file:
            fileData = data_file.readlines()
        for articleData in fileData:
            articleComponents = articleData.split("\t")
            articles[articleComponents[0]] = (Article(articleComponents[0], articleComponents[1], articleComponents[2], articleComponents[3]))
            
    return articles


# In[9]:


def pipeline(records):
    wordnet_lemmatizer = WordNetLemmatizer() 
    parser = Parser()
    for record in records:
        sentences = nltk.sent_tokenize(record)
        for sentence in sentences:
            words = nltk.word_tokenize(sentence)
            print(sentence)
            print(nltk.pos_tag(sentence))
            print parser.parse(sentence)
            for word in words:
                print("Word: ", word)
                print("Lemma: ", wordnet_lemmatizer.lemmatize(word))
                for synset in wordnet.synsets(word):
                    print (synset, synset.hypernyms())
                    print (synset, synset.hyponyms())
                    print (synset, synset.part_meronyms())
                    print (synset, synset.substance_meronyms())
                    print (synset, synset.part_holonyms())
                    print (synset, synset.substance_holonyms())

          
    print("*********")


# In[10]:


# Printing Sentences and words
articles = fetchArticles()
titles = [article.title for article in articles.values()]

pipeline(titles)


# In[8]:


from nltk.corpus import treebank
t = treebank.parsed_sents('wsj_0001.mrg')[0]
t.draw()

