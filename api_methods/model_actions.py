from datetime import datetime
from flask import make_response, abort
import json

def predict(handling_hour, created_hour, zip_code, order_cost):

    prediction = zip_code

    return make_response(json.dumps({"handling_hour" : handling_hour, "created_hour" : created_hour, "zip_code" : zip_code, "order_cost" : order_cost}))
