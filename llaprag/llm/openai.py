from llama_index.core import Settings
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI

from llaprag.settings import settings


class LLMOpenAI:
    """Initializes the OpenAI LLM and embedding configuration."""

    @classmethod
    def init(cls):
        llm = OpenAI(
            model="gpt-3.5-turbo",
            timeout=settings.llm.timeout,
        )
        embedding_model = OpenAIEmbedding(model="text-embedding-3-small")

        Settings.llm = llm
        Settings.embed_model = embedding_model
