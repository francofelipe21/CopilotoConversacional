import gradio as gr
from controller import ask_agent_response

gr.ChatInterface(
    fn=ask_agent_response,
    type="messages",
    title="Copiloto Conversacional sobre Documentos",
    multimodal=True,
    textbox=gr.MultimodalTextbox(
        file_count="multiple",
        file_types=[".pdf"]
    )
).launch()