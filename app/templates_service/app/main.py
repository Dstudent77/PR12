from fastapi import FastAPI, HTTPException
from app.template import Template


templates: list[Template] = [
    Template(100, 'First doc', 'Content'),
    Template(101, 'Second doc', 'Long, long, long, long, long, long, long, long, long, long text'),
    Template(102, 'Third doc', 'Moscow, London, Tokyo, Paris')
    
]

app = FastAPI()


@app.get("/v1/templates")
async def get_docs():
    return templates

@app.get("/v1/templates/{id}")
async def get_docs_by_id(id: int):
    result = [item for item in templates if item.id == id]
    if len(result) > 0:
        return result[0]
    
    raise HTTPException(status_code=404, detail="Template not found")