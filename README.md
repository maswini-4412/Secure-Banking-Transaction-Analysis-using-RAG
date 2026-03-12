# Secure-Banking-Transaction-Analysis-using-RAG

## Project Overview

This project implements a **Retrieval-Augmented Generation (RAG)** system to securely analyze and answer queries related to banking transactions.

The system retrieves relevant banking information from a vector database and uses a language model to generate accurate responses. This approach improves the reliability of AI-generated answers by grounding them in real data.

---

## Tech Stack

* **Python**
* **LangChain**
* **ChromaDB** (Vector Database)
* **OpenAI / LLM**
* **Gradio** (User Interface)

---

## Features

* Secure transaction query system
* Retrieval-Augmented Generation (RAG) pipeline
* Vector database using **ChromaDB**
* Prompt engineering for accurate responses
* Interactive user interface using **Gradio**

---

## Project Architecture

1. Load banking transaction data
2. Split documents into smaller chunks
3. Convert text into embeddings
4. Store embeddings in **ChromaDB vector database**
5. Retrieve relevant documents based on user query
6. Send retrieved context + query to the language model
7. Generate a final response

---

## Folder Structure

project_folder/
│
├── app.py                # Main application
├── requirements.txt      # Dependencies
├── prompts/              # Prompt templates
├── data/                 # Transaction data
├── notebooks/            # Development notebooks
└── chroma_db/            # Vector database storage

---

## How to Run the Project

### 1 Install dependencies

pip install -r requirements.txt

### 2 Run the application

python app.py

### 3 Open the interface

The application will start and provide a **Gradio interface** where users can enter banking-related queries.

---

## Example Query

* "Show recent high-value transactions"
* "Explain unusual transactions in the dataset"
* "Summarize customer transaction patterns"

---

## Future Improvements

* Add stronger security validation
* Improve query filtering
* Support real-time banking datasets
* Add authentication for sensitive queries

---

## Author

Aswani
