# ConsultBot_LLM
RAG based LLM using Dify for practicing consulting case studies

Here is the link to my application :

## If I had a minute to explain you RAG LLM concepts :

You ask something to chatgpt (prompt it) and it returns the answer. 

But it might not have the latest information, or private information (eg - company internal documents)

So we can add this required information to the prompt .

If we didnt give this information , its called 0 shot learning . If we give 1 example and then ask a question then its 1 shot learning. Otherwise its multishot learning .

But now the problem is that the prompt length to an LLM can be of limited size only (measured in tokens), whereas company internal documents can be of huge size.

So we need a system to search the part of the documents (knowledge base) related to the query (question) asked by the user, and then add that part as context to the prompt in LLM.

But this search would be slow and unstructured. 

So our pdfs (knowledge base) is broken into chunks, then we converted into vectors , then this is stored into vector database. (vector db) . Then there is a similarity search algorithm (LSH based maybe) which gets the relevent context for the query from the vector db which is added to the prompt . 

Mentos ?

## Dev side of things - 

ML models are made in tensorflow or pytorch 

Large companies like OpenAI , HuggingFace have their own LLM trained on big data using RLHF (Reinforcement Learning Using Human Feedback) which is availaible as API (Application Programming Interface) 
OpenAI API is not free, but Huggingface API is free as of now (dec 2023)

There are libraries to convert knowledge base to vector database like Chroma DB, Pinecone etc 

There is algorithm and library called FAISS (Facebook AI Simlarity Search) which help in searching parts of vector db of knowledge base relevent to the query asked by the user 

There are libraries for making frontend 


