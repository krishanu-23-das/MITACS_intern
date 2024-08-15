# Stage 1:
At stage 1 I made a basic chatbot to chat with PDFs, using RAG (Retrieval Augmented Generation), it was a basic chatbot

# Stage 2
In stage 2, I learned about LlamaIndex, a library through which you can integrate LLMs into your chatbots. I learned about the concepts of Agents and Tools.
this is the link to the official documentation: [https://docs.llamaindex.ai/en/stable/use_cases/]

# Stage 3
In stage 3, I created a query engine pipeline from Llamaindex, which can generate outputs by generating Python codes based on the query given and output a reasonable response, which can be textual information or some graphs.

# Stage 4
This stage includes fine-tuning various LLMs like the llama-7b-chat model and Gemini models by collecting responses generated from the Python query engine and uploading the input and output pair in HuggingFace.
DataFrane specific dataset: [https://huggingface.co/datasets/krishanu23/text-to-python]
General Python code Dataset: [https://huggingface.co/datasets/Vezora/Tested-143k-Python-Alpaca/viewer?row=0]

# Stage 5
In this stage i would be training Gemma model on Lora using custom defined datasets, which includes custom stastical models
