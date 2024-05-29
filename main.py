import pickle

import numpy as np
import uvicorn
from fastapi import FastAPI

from src import links
from xgboost import XGBClassifier

app = FastAPI()

with open('src/xgb_model (2).pkl', 'rb') as model_file:
    model = pickle.load(model_file)


@app.post("/predict/{url}")
async def root(url: str):
    print(url)
    numerical_values = links.numeric_value(url)
    prediction_int = np.array(list(numerical_values.values())).reshape(1, -1)
    models = model.predict(prediction_int)
    return {"prediction": int(models[0])}



if __name__ == "__main__":
    uvicorn.run(app, port=30000)
