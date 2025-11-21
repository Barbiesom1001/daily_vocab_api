from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import words, practice, stats
from app.database import engine, Base
from app.schemas import WordResponse

try:
    Base.metadata.create_all(bind=engine) 
    print("Database tables created successfully or already exist.")
except Exception as e:
    print(f"Error creating database tables: {e}") 

app = FastAPI(
    title="Vocabulary Practice API",
    version="1.0.0",
    description="API for vocabulary practice and learning"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(words.router, prefix="/api", tags=["words"])
app.include_router(practice.router, prefix="/api", tags=["practice"])
app.include_router(stats.router, prefix="/api", tags=["stats"]) # <-- ADDED

@app.get("/")
def read_root():
    return {
        "message": "Vocabulary Practice API",
        "version": "1.0.0",
        "endpoints": {
            "random_word": "/api/word",
            "validate": "/api/validate-sentence",
            "summary": "/api/summary",
            "history": "/api/history"
        }
    }
