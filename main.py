
#fastapi:
'''Instalado fastapi y Uvicorn con pip'''
#comando para empezar la API: uvicorn main:app --reload
#import asyncio
#import datetime
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
app = FastAPI()

class item(BaseModel):
     id: int 
     ingredientes: str

"""
#Python
from typing import Optional

#Pydantic
from pydantic import BaseModel

#FastAPI
from fastapi import FastAPI
from fastapi import Body

#iniciamos FastApi
app = FastAPI()

#Creamos un modelo que vamos a usar de pruebas
#Tenemos que pasar por parametro a BaseModel una class de pydantic

class Item(BaseModel):
    name: str
    price: float

#llamada al home de la API
@app.get("/")  
def home():  
	return { "mensaje" : "Hola mundo" }

#llamada que va path items y que tome el item_id que estamos pasando como Path parameter
@app.get("/items/{item_id}")
def get_item( 
		item_id: int, 
		q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

#llamada para crear un nuevo item
@app.post("/items/new")
def create_items(items: Items = Body(...)): 
    return items


#llamada para actualizar un item en específico. 
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}"""

'''asyncio is used as a foundation for multiple Python 
asynchronous frameworks that provide high-performance 
network and web-servers, database connection libraries, 
distributed task queues, etc.'''
# asyncio.sleep(1) # duerme 1 second

''' Asíncrono es "concurencia" (se usa todo
lo disponible: busca ser lo mas eficiente posible
todo el ratos, si tienes que esperar estas ocioso, 
asique mientras no se ocupan recursos se usan para
otra cosa) para cuando no hay q sincronizar 
nada, es decir no hay que esperar una respuesta de ningun sitio
en este caso son ejemplos y no hay que comunicarse con un 
servidor "async def" también se usa await'''
###################################################################
'''await tiene que estar dentro de una funcion async def'''
"""
'''
async def get_burguers(burguers: int):  
    await asyncio.sleep(1)
    return {burguers}

burgers = get_burguers(2)
print("hay " + burgers + "burguers")
'''
''' Síncrono es cuando hay que esperar respuestas y se usa 
solo "def" '''
"""


#POST para crear un recurso del servidor
#llamada para crear un nuevo item

@app.post("/recursos/{recurso_id}")
async def prueba_post_crear_item(recurso_id: int,  q: Optional[str]=None):
    results = {"recurso_id": recurso_id, "q": q}
    return results # + {"message": "se ha registrado una hamburguesa"}

#OPTIONS opciones de comunicación para el 
# recurso de destino.
@app.options("/")
async def prueba_options(id):
    return {"message": "esto es una prueba"}

#PUT para actualizar un recurso del servidor
@app.put("/")
async def prueba_put(id):
    return {"message": "esto es una prueba"}

#PATCH hace modificaciones parciales a un recurso.
@app.patch("/")
async def prueba_patch(id):
    return {"message": "esto es una prueba"}

#GET para obtener un recurso del servidor
@app.get("/recursos/{recurso_id}")
async def prueba_get(recurso_id: int, q: Optional[str]=None):
    results = {"recurso_id" : recurso_id, "q" : q}
    return results

#Es un GET sin el cuerpo de respuesta ???
@app.head("/")
async def prueba_head(id):
    return {"message": "esto es una prueba"}

#DELETE para eliminar un recurso del servidor
@app.delete("/")
async def prueba_delete(id):
    return {"message": "esto es una prueba"}

#TRACE  realizar una prueba de bucle invertido
#de mensajes que prueba la ruta del recurso 
# e destino (útil para fines de depuración).
@app.trace("/")
async def prueba_trace(id):
    return {"message": "esto es una prueba"}
#connect¿¿¿???
'''
para iniciar la api poner en consola:
uvicorn main:app --reload 

se encuentra en la direccion http://127.0.0.1:8000/
IMPORTANTE: Aquí esta la API http://127.0.0.1:8000/docs
'''
#pytest
from unittest import TestCase

class TryTesting(TestCase):
    def test_always_passes(self):
        self.assertTrue(True)

    def test_always_fails(self):
        self.assertTrue(False)

#Por consola:
# python -m unittest discover