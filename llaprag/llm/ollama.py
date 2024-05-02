from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

from llaprag.settings import settings


class LLMOLlama:
    """Initializes the Llama LLM and embedding configuration."""

    @classmethod
    def init(cls):
        llm = Ollama(
            base_url="http://localhost:11434",
            model=settings.llm.model,
            request_timeout=settings.llm.timeout,
        )
        embedding_model = HuggingFaceEmbedding(model_name=settings.chroma.embedding_model)

        Settings.llm = llm
        Settings.embed_model = embedding_model
