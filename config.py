# api_key='92024ca524b9462782a214ac25c41263'
# BASE_URL='https://newsapi.org/v2/sources?apiKey=API_KEY'
import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_SOURCES_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    SPECIFIC_SOURCE_API_URL = 'https://newsapi.org/v2/everything?language=en&sources={}&apiKey={}'

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')