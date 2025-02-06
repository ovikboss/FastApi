import uvicorn
from fastapi import FastAPI
from ..routes.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "http://localhost",  # Разрешить доступ с этого URL
    "https://example.com",    # Разрешить доступ с этого URL
    # добавьте другие URL, если необходимо
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Список разрешенных источников
    allow_credentials=True,  # Разрешить креденциалы (если нужно)
    allow_methods=["*"],     # Разрешить все методы (GET, POST и т.д.)
    allow_headers=["*"],     # Разрешить все заголовки
)



app.include_router(router)

