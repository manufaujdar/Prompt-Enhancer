# Prompt Enhancer

A Python framework and FastAPI service for evaluating, enhancing, and optimizing
prompts before LLM API calls. The current API uses Microsoft's Promptist model
to improve the clarity and effectiveness of text prompts for AI-model
interactions.

## Features

- **Prompt Enhancement**: Transform basic prompts into more detailed, effective versions
- **RESTful API**: Clean, documented endpoints with proper error handling
- **Health Monitoring**: Built-in health check endpoint
- **CORS Support**: Ready for web frontend integration
- **Logging**: Comprehensive logging for debugging and monitoring

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Prompt-Enhancer
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

## API Endpoints

### GET `/`
Health check endpoint that confirms the API is running.

**Response:**
```json
{
  "message": "Prompt Enhancer API is running"
}
```

### GET `/health`
Detailed health check that includes model status.

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### POST `/enhance`
Enhance a prompt using the Promptist model.

**Request Body:**
```json
{
  "text": "a cat sitting on a chair"
}
```

**Response:**
```json
{
  "improved_prompt": "a beautiful cat sitting comfortably on a wooden chair",
  "original_prompt": "a cat sitting on a chair"
}
```

## Usage Examples

### Using curl
```bash
curl -X POST "http://localhost:8000/enhance" \
     -H "Content-Type: application/json" \
     -d '{"text": "a dog in a park"}'
```

### Using Python requests
```python
import requests

response = requests.post(
    "http://localhost:8000/enhance",
    json={"text": "a dog in a park"}
)
print(response.json())
```

## API Documentation

Once the server is running, you can access:
- **Interactive API docs**: http://localhost:8000/docs
- **ReDoc documentation**: http://localhost:8000/redoc

## Error Handling

The API returns appropriate HTTP status codes:
- `200`: Success
- `400`: Bad request (empty prompt)
- `500`: Internal server error
- `503`: Service unavailable (model not loaded)

## Development

### Running in Development Mode
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Environment Variables
- `PORT`: Server port (default: 8000)
- `HOST`: Server host (default: 0.0.0.0)

## Dependencies

- **FastAPI**: Modern web framework for building APIs
- **Pydantic**: Data validation using Python type annotations
- **Transformers**: Hugging Face transformers library for the Promptist model
- **PyTorch**: Deep learning framework
- **Uvicorn**: ASGI server for running FastAPI applications

## License

[Add your license information here]
