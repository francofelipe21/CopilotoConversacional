from llama_index.core import get_response_synthesizer
from llama_index.core import DocumentSummaryIndex
from llama_index.core.node_parser import HierarchicalNodeParser
from llama_index.core import VectorStoreIndex
from agent.store import storage_context
from llama_index.llms.openai import OpenAI
from agent.config import api_key

hierarchical_node_parser = HierarchicalNodeParser.from_defaults(chunk_sizes=[2048, 512, 128])

response_synthesizer = get_response_synthesizer(response_mode="tree_summarize", use_async=True)

doc_summary_index = DocumentSummaryIndex.from_documents(
        documents=[],
        llm=OpenAI(model="gpt-4o-mini"),
        api_key=api_key,
        transformations=[hierarchical_node_parser],
        response_synthesizer=response_synthesizer,
        storage_context=storage_context)

general_index = VectorStoreIndex.from_documents(documents = [], storage_context=storage_context)

def get_summary_index():
    return doc_summary_index

def get_general_index():
    return general_index