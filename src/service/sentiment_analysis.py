import os
import pickle
cur_path = os.path.dirname(os.path.realpath('__file__'))

model_path = os.path.join(cur_path, 'src/data/tfidf_model_max_iter_200_v3.pkl')
model_path = os.path.abspath(os.path.realpath(model_path))

tokenizer_path = os.path.join(cur_path, 'src/data/tfidf_vectorizer_max_iter_200_v3.pkl')
tokenizer_path = os.path.abspath(os.path.realpath(tokenizer_path))


class SentimentAnalysisService:

    def __init__(self):
        self.model = pickle.load(open(model_path, 'rb'))
        self.tfidf_vectorizer = pickle.load(open(tokenizer_path, 'rb'))

    def analyse(self, normalized_sentence):
        transformed_sentence = self.tfidf_vectorizer.transform([normalized_sentence])
        return self.model.predict(transformed_sentence)[0]
