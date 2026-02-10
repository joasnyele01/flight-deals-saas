from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI(
    title="Flight Deals API",
    description="API pour alertes vols flexibles",
    version="0.1.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "✈️ Flight Deals API is running!",
        "status": "operational",
        "version": "0.1.0",
        "endpoints": {
            "health": "/health",
            "docs": "/docs",
            "test_db": "/test-db"
        }
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "database": check_database(),
        "redis": check_redis()
    }

def check_database():
    db_url = os.getenv("DATABASE_URL")
    if db_url and "postgresql" in db_url:
        return "Connected ✅"
    return "Not configured ⚠️"

def check_redis():
    redis_url = os.getenv("REDIS_URL")
    if redis_url and "redis" in redis_url:
        return "Connected ✅"
    return "Not configured ⚠️"

@app.get("/test-db")
def test_database_connection():
    """Teste la connexion aux bases de données"""
    return {
        "database_url": os.getenv("DATABASE_URL", "NOT_SET")[:30] + "...",
        "redis_url": os.getenv("REDIS_URL", "NOT_SET")[:30] + "...",
        "database_status": check_database(),
        "redis_status": check_redis()
    }

@app.get("/api/v1/test")
def test_endpoint():
    """Endpoint de test"""
    return {
        "message": "API fonctionne parfaitement! 🚀",
        "ready_for": "flight deals implementation"
    }
