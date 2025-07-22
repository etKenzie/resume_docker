from fastapi import FastAPI
from mangum import Mangum
from router import router as process_router

app = FastAPI()
app.include_router(process_router)
handler = Mangum(app)



