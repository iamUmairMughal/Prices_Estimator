from django.apps import AppConfig
import joblib

model_reg = joblib.load('prices/RandomForest.pkl')

class PricesConfig(AppConfig):
    name = 'prices'
