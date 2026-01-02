from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.google_trends import router as google_trends_router


app = FastAPI(title="AI Trend & Opportunity Scanner API")

# Allow frontend to talk to backend during development
origins = [
	"http://localhost:3000",  # Next.js dev server
]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)


@app.get("/health")
def health_check():
	return {"status": "ok", "message": "Backend is running"}


app.include_router(google_trends_router)
