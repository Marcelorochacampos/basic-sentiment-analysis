from flask import Response, request
from flask_restful import Resource
import json

from src.service.sentence import SentenceService
from src.service.sentiment_analysis import SentimentAnalysisService


class SentimentAnalysisController(Resource):

    def __init__(self):
        self.sentence_service = SentenceService()
        self.sentiment_analysis_service = SentimentAnalysisService()

    def get(self):
        pass

    def post(self):
        data = request.get_json(force=True)

        if not 'sentence' in data or not data['sentence'].strip():
            return Response('{ "message": "Need to specify the sentence" }', status=400,
                            mimetype='application/json')

        normalized_sentence = self.sentence_service.normalize(data['sentence'])
        analysis = self.sentiment_analysis_service.analyse(normalized_sentence)

        return Response(response=json.dumps({
            "data": int(analysis)
        }), status=200, mimetype='application/json')
