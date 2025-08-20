# Execution instructions #

Python version: 3.13.3

To run the chatbot follow the steps below:
    1. Install the libraries in the file requeriments.txt
    2. In the backend folder run fastapi dev server.py
    3. In the frontend folder run python chatbot.py

## Architecture and justification of technical choices ##

The frontend folder contains the code that displays the chat window. It consists of two files: chatbot.py and
controller.py. The first handles the rendering logic and the second handles the connection to the backend.
Gradio was chosen because of its ease of use for quickly creating interfaces. One disadvantage is its lack of
flexibility, but given the project's requirements, advanced front-end customization isn't necessary.

In the backend folder, the server is initialized, and routers and controllers are created to separate the various
logic into different components, which also makes the project more extensible. Requests are made to the agent
from the backend and the response is returned to the frontend. FastAPI was chosen for its ability to easily
parallelize API calls with "async's" and "await's", which was useful when parallelizing PDF indexing.

The agent folder contains all the agent logic. Each RAG agent has the ability to vectorize, save and create
query engines from the processed documents. Each of these functions has its own file in which they are performed.
Llamaindex was the orchestration framework chosen for its low learning curve compared to LangChain and because 
it is oriented towards RAG agents.

## Explanation of conversational flow ##

A message is received in the conversational interface and it is evaluated based on its content. Depending on 
the content, a specific POST request is made and a response is received from the server. If the message 
received is a text message, the backend invokes the agent to process it. If the message received is a document, 
the backend transforms the binary into a PDF, which Llamaindex processes, vectorizing it and saving it to the 
database. This database is used to create indexes and query engines so that the agent has tools to use if it 
receives a query about PDFs, for example a summary.

## Current limitations ##

Among the main limitations are that Copilot is slow to process PDFs, can suffer from hallucinations, and runs 
the risk of disclosing personal information, as it has no filtering system for what information it can retrieve 
from the database.

## Future improvements ##

Integrate a model that specializes in detecting hallucinations and another that specializes in detecting 
sensitive information. In addition to the above, the project could also be improved by adding document 
comparison and classification functionality. For the first task, I would create an index for each document, 
which could be compared by an LLM. For the second task, I would create clusters for the documents and, using 
the k-means algorithm and a set of representative documents per category, the category of each document could 
be classified.

