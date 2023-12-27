# ConsultBot_LLM
RAG based LLM using Dify for practicing consulting case studies

![consultbot_trial_1](https://github.com/ayush-agarwal-0502/ConsultBot_LLM/assets/86561124/a26a0713-89e8-4caa-b000-6828f0567740)

Here is the link to my application hosted on DiFy cloud : https://udify.app/chat/I91qkxLZaxCOGHKY 

(Please don't overuse it I don't have OpenAI credits so one person's greed will make it stop working for everyone)(Thank You) 

## My Idea and Vision :

I was studying for placements and I realized that there is so much support availaible for SDE, yet so less of practice material curated specially for Business and related Domains (Consulting, Analytics, Product Management). I validated this observed population pain point by talking to my friends . As I was studying about RAG in LLM and its applications it struck to me that I could solve my friends problems : All I had to do was download casebooks (which are free and open source) from the IIMs, and deploy a RAG based LLM application to allow the users to practice case studies by talking to the chatbot. As the vision became clearer to me, I started working upon my idea :)  

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

Oh and by the way , RAG LLM means Retrival Augmented Generation for Large Language Models . You can see the research paper here - https://arxiv.org/abs/2005.11401

## Dev side of things - 

ML models are made in tensorflow or pytorch 

Large companies like OpenAI , HuggingFace have their own LLM trained on BigData using RLHF (Reinforcement Learning Using Human Feedback) which is availaible as API (Application Programming Interface) 
OpenAI API is not free, but Huggingface API is free as of now (dec 2023)

There are libraries to convert knowledge base to vector database like Chroma DB, Pinecone etc 

There is algorithm and library called FAISS (Facebook AI Simlarity Search) which help in searching parts of vector db of knowledge base relevent to the query asked by the user . You can see the details here - https://ai.meta.com/tools/faiss/

There are libraries for making frontend part of chatbot such as StreamLit and Flask

There are PDF reading libraries to smoothen the data reading part too

There are libraries to manage the whole RAG setup - LangChain

## Appreciation Note for Dify and Explanation for the abstraction layers - 

First Data Scientists made models using programming 

Then Libraries like Tensorflow and Pytorch came so that coding a neural network was no longer a rocket science. A layer of abstraction. 

Then Large companies made their models and started selling the API access, and any developer could call these APIs to use ML model without bothering about the "ML Part" of it . Another layer of abstraction.

Then RAG came, and all the libraries came which I have described here. 

But the Last layer of Abstraction is Dify . More details availaible on their website - https://dify.ai/ and https://cloud.dify.ai/apps. It allows to setup a RAG based pipeline very conveniently, giving the freedom to set the required hyperparameters , make a knowledge base, choose the models we need, choose vector db, editing the frontend etc. It was created sometime in 2023, and the company is much much more than a chatgpt wrapper , and I feel it will be the next popular layer of abstraction. 




