import sys

from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage
from llama_index.core.indices.base import BaseIndex
from llama_index.core.vector_stores.types import BasePydanticVectorStore
from llama_index.vector_stores.chroma import ChromaVectorStore

from llaprag.settings import settings


class VSChromaDB:
    """Initializes the ChromaDB Vector Store."""

    def __init__(self):

        # User Documents and Nodes for storing
        # https://docs.llamaindex.ai/en/latest/module_guides/loading/documents_and_nodes/
        self.chroma_store: BasePydanticVectorStore = ChromaVectorStore(
            host=settings.chroma.host,
            port=settings.chroma.port,
            collection_name=settings.chroma.collection_name,
        )

    def create_index(self, storage_context: StorageContext) -> BaseIndex:
        """Initialize the vector store index. If the index is not found in storage, create a new one."""
        try:
            return load_index_from_storage(storage_context)
        except ValueError as err:
            if (
                str(err)
                == "No index in storage context, check if you specified the right persist_dir."
            ):
                index = VectorStoreIndex.from_vector_store(storage_context.vector_store)
                index.storage_context.persist()
                return index
            else:
                sys.exit()
        except Exception:
            sys.exit()
