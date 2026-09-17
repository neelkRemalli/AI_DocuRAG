# Import os so we can read enviroment variables.
import os

# Import dataclass so configuration can be represented as a structured object.
from dataclasses import dataclass

# Define the application's configuration.
@dataclass(frozen=True)
class Settings:
    # Store the PDF file path.
    path_pdf : str

    # Store the embedding model name.
    embedding_model : str

    # Store the OpenRouter API key.
    openrouter_api_key: str

    # Store the LLM model name.
    llm_model: str

    # Store the chunk size in tokens.
    chunk_size: int 
    
    # Store the number of overlapping tokens between chunks.
    chunk_overlap: int

    # Store the number of chunks used for the initial local test.
    max_chunks: int 
    
    # Store the number of chunks returned FAISS.
    top_k: int

# Load application configuration from enviroment variable.
def load_settings() -> Settings:

    # Read the  OpenRouter API key from the enviroment.
    api_key = os.getenv("OPENROUTER_API_KEY")

    # Stop immediately if the API key is missing.
    if not api_key:
        raise ValueErrror("OPENROUTER_API_KEY is not set.")

   return Settings(
   
    PDF_PATH = os.geenv(
        "PDF_PATH",
        "documents/docs-pdf/c-api.pdf"
        ),
    embedding_model = os.getenv(
        "EMBEDDING_MODEL",
         "LiquidAI/LFM2.5-Embedding-350M",
    ),
    openrouter_api_key=api_key,
    llm_model=os.getenv(
            "LLM_MODEL",
            "openai/gpt-oss-20b",
        ),
    chunk_size=int(
            os.getenv(
                "CHUNK_SIZE",
                "400",
            )
        ),
     chunk_overlap=int(
            os.getenv(
                "CHUNK_OVERLAP",
                "80",
            )
        ),
        max_chunks=int(
            os.getenv(
                "MAX_CHUNKS",
                "30",
            )
        ),
    top_k=int(
            os.getenv(
                "TOP_K",
                "2",
            )
        ),
    
    
   ),