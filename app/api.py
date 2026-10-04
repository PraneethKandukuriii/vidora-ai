from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from .ingestion import process_video
from .rag import answer_question


app = FastAPI(
    title="Vidora API",
    description="AI-powered YouTube chatbot",
    version="1.0.0",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://vidora-ai-two.vercel.app",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class VideoRequest(BaseModel):
    video_url: str = Field(..., min_length=1)


class QuestionRequest(BaseModel):
    question: str = Field(..., min_length=1)


current_vector_store = None


@app.get("/")
def root():
    return {
        "success": True,
        "message": "Vidora API is running",
    }


@app.post("/process-video")
def process_video_endpoint(request: VideoRequest):
    global current_vector_store

    video_data = process_video(request.video_url)

    current_vector_store = video_data["vector_store"]

    return {
        "success": True,
        "message": "Video processed successfully",
        "video_id": video_data["video_id"],
        "transcript_length": len(video_data["transcript"]),
        "chunks": len(video_data["chunks"]),
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):
    if current_vector_store is None:
        return {
            "success": False,
            "message": "Please process a video first.",
        }

    answer = answer_question(
        vector_store=current_vector_store,
        question=request.question,
        chat_history=[],
    )

    return {
        "success": True,
        "answer": answer,
    }