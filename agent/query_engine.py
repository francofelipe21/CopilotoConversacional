from llama_index.core.indices.document_summary import DocumentSummaryIndexLLMRetriever
from llama_index.core import get_response_synthesizer
from llama_index.core.query_engine import RetrieverQueryEngine
from agent.index import get_general_index, get_summary_index

def get_general_query_engine():
    index = get_general_index()
    query_engine = index.as_query_engine()
    return query_engine

def get_summary_query_engine():
    index = get_summary_index()
    retriever = DocumentSummaryIndexLLMRetriever(
        index
    )
    response_synthesizer = get_response_synthesizer(response_mode="tree_summarize")
    query_engine = RetrieverQueryEngine(
        retriever=retriever,
        response_synthesizer=response_synthesizer,
    )
    return query_engine