import logging
import uvicorn
from fastapi import FastAPI
from app.routes import router


logging.basicConfig(
    level=logging.INFO,  # Establece el nivel de logging (puedes ajustarlo según tus necesidades)
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.StreamHandler()  # Agrega un handler para imprimir los logs en la consola
    ]
)


app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app = app,host='0.0.0.0',reload=True)