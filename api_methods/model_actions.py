from datetime import datetime
from flask import make_response, abort
import json
from inference_model import model
import numpy as np
from keras.utils import to_categorical

def predict(handling_hour, created_hour, zip_code, order_cost):
    prediction = int(model.predict(verbose=1, x=np.array([[created_hour, handling_hour, int(zip_code), order_cost]]))[0][0])
    return make_response(json.dumps({"ht_real" : prediction}))
