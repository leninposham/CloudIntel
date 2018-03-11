from sklearn.externals import joblib
from django.conf import settings
import os

class LoadModel():

    def __init__(self, pickle_name):
        self.model = joblib.load(os.path.join(getattr(settings, "MODELS_DIR"),pickle_name))