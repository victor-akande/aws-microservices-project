from fastapi import FastAPI
import uvicorn
from mylib.logic import summary as summary_logic
from mylib.logic import search as search_logic
from mylib.logic import phrases as phrases_logic

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /summary or /search or /phrases"}


@app.get("/search/{value}")
async def search(value: str):
    """Page to search in Wikipedia"""

    result = search_logic(value)
    return {"results": result}


@app.get("/summary/{value}")
async def summary(value: str):
    """Retreive the summary of a Wikipedia page"""

    result = summary_logic(value)
    return {"result": result}


@app.get("/phrases/{name}")
async def phrases(name: str):
    """Retrieve and return phrases from a Wikipedia page"""

    result = phrases_logic(name)
    return {"result": result}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
