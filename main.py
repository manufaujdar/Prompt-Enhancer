from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Prompt Enhancer API",
    description="An API to enhance prompts using Microsoft's Promptist model",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model once
try:
    logger.info("Loading Promptist model...")
    enhancer = pipeline("text2text-generation", model="microsoft/promptist")
    logger.info("Model loaded successfully")
except Exception as e:
    enhancer = None
    logger.error(f"Failed to load model: {e}")

class PromptRequest(BaseModel):
    text: str
    
    class Config:
        schema_extra = {
            "example": {
                "text": "a cat sitting on a chair"
            }
        }

class PromptResponse(BaseModel):
    improved_prompt: str
    original_prompt: str

@app.get("/")
async def root():
    return {"message": "Prompt Enhancer API is running"}

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "model_loaded": enhancer is not None
    }

@app.post("/enhance", response_model=PromptResponse)
async def enhance_prompt(req: PromptRequest):
    if enhancer is None:
        raise HTTPException(
            status_code=503, 
            detail="Model not loaded. Please try again later."
        )
    
    if not req.text.strip():
        raise HTTPException(
            status_code=400, 
            detail="Prompt text cannot be empty"
        )
    
    try:
        logger.info(f"Enhancing prompt: {req.text[:50]}...")
        result = enhancer(req.text, max_new_tokens=128)[0]["generated_text"]
        logger.info("Prompt enhanced successfully")
        
        return PromptResponse(
            improved_prompt=result,
            original_prompt=req.text
        )
    except Exception as e:
        logger.error(f"Error enhancing prompt: {e}")
        raise HTTPException(
            status_code=500, 
            detail=f"Failed to enhance prompt: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    