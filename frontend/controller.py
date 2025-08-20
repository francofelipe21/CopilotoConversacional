import requests
import json

error_message = "There was an error"

def decode_response(response):
    response = response.content
    response = response.decode("utf-8")
    response = json.loads(response)
    return response

def getAgentResponse(text):
    response = requests.post(" http://127.0.0.1:8000/new_user_message", json={"msg": text})
    response = decode_response(response)
    return response

def ask_agent_response(message, history):
    text = message["text"]
    files = message["files"]
    len_text = len(text)
    num_pdfs = len(files)
    if num_pdfs > 5 or (num_pdfs == 0 and len_text == 0):
        return {"text" : error_message}
    else:
        if len_text > 0 and num_pdfs == 0:
            return getAgentResponse(text)
        if num_pdfs > 0:
            file_data = []
            for file in files:
                file_data.append(("files", (file, open(file, "rb"), "application/pdf")))
            response = requests.post(" http://127.0.0.1:8000/upload_pdfs", files=file_data)
            if response.status_code < 400:
                response = {"text" : "PDF procesado exitosamente.\n"}
                if len_text>0:
                    response["text"] += getAgentResponse(text)["text"]
            else:
                response = {"text" : error_message}
            return response
        else:
            return {"text" : error_message}