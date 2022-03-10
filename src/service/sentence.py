import nltk
from nltk import tokenize
from string import punctuation
from unidecode import unidecode
nltk.download('stopwords')
nltk.download('rslp')


class SentenceService:

    def __init__(self):
        self.word_punct_tokenizer = tokenize.WordPunctTokenizer()
        self.stopwords = nltk.corpus.stopwords.words('portuguese')
        self.punctuation = list(i for i in punctuation)
        self.stemmer = nltk.RSLPStemmer()

    def normalize(self, sentence):
        tokenized_sentence = self.word_punct_tokenizer.tokenize(sentence)
        normalized_sentence = list()

        for word in tokenized_sentence:
            word = unidecode(word.lower())
            if (word not in self.stopwords) and (word not in self.punctuation):
                normalized_sentence.append(self.stemmer.stem(word))

        return ' '.join(normalized_sentence)