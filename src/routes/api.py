from flask import current_app
from src import api, api_bp

from src.controller.api.sentiment_analysis import SentimentAnalysisController

api.add_resource(SentimentAnalysisController, '/sentence/analyse', '/sentence/analyse')
