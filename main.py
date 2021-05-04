from fastapi import FastAPI, Query
from typing import Optional
from pydantic import BaseModel
from fastapi.logger import logger


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.get('/items/')
async def get_items(q: str = Query(..., min_length=5, max_length=50, regex="^fixedquery$")):
    try:
        results = [{"item_id": "Foo"}, {"item_id": "Bar"}]
        if q:
            logger.info(type(q))
            results.append({"q": q})
        return results
    except AttributeError as e:
        logger.warning(msg=e)


@app.post('/items/')
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = round(item.price + item.tax, 2)
        item_dict.update({"price_with_tax": price_with_tax})

    return item_dict


@app.put('/items/{item_id}')
async def update_or_create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


@app.delete('/items/{item_id}')
async def delete_item(item_id: int, q: Optional[str] = None):
    pass
