from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"ФИО": "Таран Анна Вячеславовна"}

@app.get('/users')
async def f_indexT():
    return "+79130259379"

@app.get('/tools')
async def f_indexT():
    return "Навыки разработчика в процессе формирования"