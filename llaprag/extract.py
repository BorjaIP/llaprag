from llama_index.core import SimpleDirectoryReader
from llama_parse import LlamaParse
from llama_parse.utils import ResultType

from llaprag.document import DocumentService
from llaprag.download import download_paper
from llaprag.index.redis import IndexRedis
from llaprag.llm.ollama import LLMOLlama
from llaprag.llm.openai import LLMOpenAI
from llaprag.paper import Paper
from llaprag.vector_store.chromadb import VSChromaDB

api_key = "llx-CwHqcHgcyTqqZampLsVILiG8gIRMlcMEGrWj8L0B4sAI0XsF"


def extract_nodes(paper: Paper, llm: str):
    # Indexing in LLamaIndex
    # https://docs.llamaindex.ai/en/v0.9.48/module_guides/indexing/index_guide.html

    # use this to set custom chunk size and splitting
    # https://docs.llamaindex.ai/en/stable/module_guides/loading/node_parsers/

    parser = LlamaParse(
        api_key=api_key,
        result_type=ResultType.MD,
        # num_workers=4,  # if multiple files passed, split in `num_workers` API calls
    )
    file_extractor: dict = {".pdf": parser}
    documents = SimpleDirectoryReader(
        str(paper.path.parent), file_extractor=file_extractor
    ).load_data()

    print("llm init")
    if llm == "ollama":
        LLMOLlama.init()
    elif llm == "openai":
        print("llm - openai")
        LLMOpenAI.init()
    else:
        pass

    print("init storage")
    vector_store = VSChromaDB()
    print("init redis")
    index_store = IndexRedis()

    document = DocumentService(parser=parser)
    index = document.create_index(vector_store=vector_store, index_store=index_store)
    print("save data")
    document.save_data(documents, index)

    # Create query engine

    # streaming_query_engine: BaseQueryEngine = index.as_query_engine(
    #     streaming=True, similarity_top_k=10
    # )

    # Query index
    print("query engine")
    query_engine = index.as_query_engine()
    response = query_engine.query("Extract the title of the paper")
    print("Extract the title of the paper")
    print(response)


if __name__ == "__main__":
    url = "https://arxiv.org/pdf/2303.18223.pdf"
    paper = download_paper(url)
    extract_nodes(paper, llm="openai")
