from agent.query_engine import get_general_query_engine, get_summary_query_engine

async def answer_question_pdf(query: str) -> str:
    """Retrieves relevant information to answer questions related to uploaded documents"""
    print("general")
    query_engine = get_general_query_engine()
    response = query_engine.query(query)
    return str(response)

async def ask_summary(query: str) -> str:
    """summarize a pdf"""
    print("summary")
    query_engine = get_summary_query_engine()
    response = query_engine.query(query)
    return str(response)
