from typing import Union

import uvicorn
from fastapi import FastAPI

from model.models import *


app = FastAPI()
# data = get_data('insurance')
# s = setup(data, target='charges')
# best = compare_models()
# create_api(best, 'insurance_prediction_model')


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/updateItem/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}

@app.post('/predict')
def predict(age, sex, bmi, children, smoker, region):
    return 'Hello'




if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=10000)
