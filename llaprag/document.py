
from llama_index.core import Settings, StorageContext
from llama_index.core.indices.base import BaseIndex
from llama_index.core.node_parser import MarkdownElementNodeParser
from llama_index.core.schema import Document
from llama_parse import LlamaParse

from llaprag.index.redis import IndexRedis
from llaprag.vector_store.chromadb import VSChromaDB


class DocumentService:
    """Utility class for saving data into an index."""

    def __init__(self, parser: LlamaParse) -> None:
        self.parser = parser
        self.node_parser = MarkdownElementNodeParser(llm=Settings.llm, num_workers=8)

    def save_data(self, documents: list[Document], index: BaseIndex) -> None:
        """Save data into the given index."""

        nodes = self.node_parser.get_nodes_from_documents(documents)
        base_nodes, objects = self.node_parser.get_nodes_and_objects(nodes)

        index.insert_nodes(base_nodes + objects)
        index.storage_context.persist()

    def create_index(self, vector_store: VSChromaDB, index_store: IndexRedis) -> BaseIndex:
        """Create an index."""
        # Store Nodes, indices and vectors
        # https://docs.llamaindex.ai/en/stable/api_reference/storage/storage_context/
        storage_context = StorageContext.from_defaults(
            vector_store=vector_store.chroma_store, index_store=index_store.redis_store
        )

        index: BaseIndex = vector_store.create_index(storage_context)
        return index
