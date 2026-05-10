from fastapi import FastAPI

app = FastAPI(
    title="Ticket System API",
    description="MVP backend for a ticket system portfolio project",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "Ticket System API is running 🚀"}

@app.get("/health")
def health_check():
    return {"status": "ok"}