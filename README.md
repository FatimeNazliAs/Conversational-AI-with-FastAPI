# Conversational AI Platform Backend

This project is a backend system for a conversational AI platform using FastAPI, SQLAlchemy ORM, and GPT-based models. The system is designed to handle message processing, document management, and AI response generation for food and weather queries.

## Current Progress

### 1. **API Endpoints**:

- **POST /messages**: 
  - **Message Classification**: The message is classified as either a food or weather query.
  - **Weather Queries**: 
    - Weather data for New York City is fetched using the Weather API.
    - Weather details are converted to natural language using GPT-4, following a structured prompt for varied types of questions.
  - **Food Queries**: 
    - Food-related queries will be processed using Llama 3.3-70b-versatile with Retrieval-Augmented Generation (RAG) — this step is pending implementation.

- **POST /documents**:
  - **Document Upload**: Documents are successfully uploaded to the system and stored in the designated folder.
  - **PDF Processing**: Document processing is not yet implemented, which includes splitting into pages and chunking content.
  - **Vectorization**: Document chunks are intended to be embedded using OpenAI’s text-embedding-3-small model and stored in ChromaDB — this integration is pending.

### 2. **Weather API Integration**:
- Successfully integrated the Weather API to fetch data for New York City.
- Data is parsed and displayed in a simplified manner with a focus on natural language responses using GPT-4.

### 3. **.env Configuration**:
- Environment variables are managed using the `dotenv` library.
- Weather API key and Open AI key have been added to `.env` for secure API integration.

## Future Tasks

### 1. **Food Queries (POST /messages)**:
   - Implement food-related query classification and response generation.
   - Integrate **Llama 3.3-70b-versatile** with RAG for processing and answering food-related queries.

### 2. **Document Management (POST /documents)**:
   - Implement document chunking and embedding using OpenAI’s text-embedding-3-small model.
   - Set up **ChromaDB** for vector storage of document embeddings.
   - Process uploaded documents (split into pages, chunk content, and embed using embeddings).

## Setup Instructions

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/conversational-ai-platform.git
```

### 2. Install the required dependencies:
```bash
cd conversational-ai-platform
pip install -r requirements.txt
```

### 3. Set up environment variables:
Create a `.env` file in the root directory of the project and add your Weather API key:
```text
WEATHER_API_KEY=your-weather-api-key
OPEN_AI_KEY=your-openai-key
```

### 4. Run the FastAPI server:
```bash
uvicorn main:app --reload
```
This will start the FastAPI server locally.


