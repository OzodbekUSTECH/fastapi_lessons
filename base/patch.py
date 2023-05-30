# from fastapi import FastAPI
# from fastapi.encoders import jsonable_encoder
# from pydantic import BaseModel

# app = FastAPI()


# class Item(BaseModel):
#     name: str | None = None
#     description: str | None = None
#     price: float | None = None
#     tax: float = 10.5
#     tags: list[str] = []


# items = {
#     "foo": {"name": "Foo", "price": 50.2},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
#     "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
# }


# @app.get("/items/{item_id}", response_model=Item)
# async def read_item(item_id: str):
#     return items[item_id]


# @app.patch("/items/{item_id}", response_model=Item)
# async def update_item(item_id: str, item: Item):
#     stored_item_data = items[item_id] #извлек
#     stored_item_model = Item(**stored_item_data) #поместил в модель
#     update_data = item.dict(exclude_unset=True) #Сгенерируйте значение без значений по умолчанию из входной модели (с помощью ).dictexclude_unset
#     updated_item = stored_item_model.copy(update=update_data) #Создайте копию хранимой модели, обновив ее атрибуты полученными частичными обновлениями (с помощью параметра).update
#     items[item_id] = jsonable_encoder(updated_item) #Преобразуйте скопированную модель во что-то, что может храниться в вашей БД (например, с помощью ).jsonable_encoder
#     return updated_item #Преобразуйте скопированную модель во что-то, что может храниться в вашей БД (например, с помощью ).jsonable_encoder