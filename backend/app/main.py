from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Competitor Listener API",
    description="AI-powered competitor intelligence from public sources",
    version="0.1.0",
)

# Allow React frontend to talk to backend during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Competitor Listener API is live! 🚀"}


@app.get("/health")
def health():
    return {"status": "healthy"}
