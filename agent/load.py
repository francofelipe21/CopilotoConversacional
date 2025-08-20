from llama_index.core.node_parser import HierarchicalNodeParser
from llama_index.core import SimpleDirectoryReader
from llama_index.core.ingestion import IngestionPipeline
from agent.index import get_general_index, get_summary_index

async def insert_new_document(filename):
    try:
        document = SimpleDirectoryReader(input_files=["./uploaded_pdfs/" + filename]).load_data()[0]
        general_index = get_general_index()
        summary_index = get_summary_index()
        general_index.insert(document)
        summary_index.insert(document)
        return {"status_code":200}
    except:
        return {"status_code":500}

