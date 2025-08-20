from agent.store import storage_context
from agent.config import api_key
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.workflow import Context
from agent.tools import answer_question_pdf, ask_summary
from agent.config import api_key

agent = FunctionAgent(
    tools=[answer_question_pdf, ask_summary],
    llm=OpenAI(model="gpt-4o-mini"),
    api_key=api_key,
    system_prompt="You are a helpful assistant that can analyze documents.",
)
ctx = Context(agent)
