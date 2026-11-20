# ChromaDB Vector Search using Gemini Embeddings

## About the Project

While learning about LLMs and RAG, I wanted to understand how text embeddings are stored and how applications retrieve relevant information from them.

So, I built this small project using Google's Gemini Embedding API and ChromaDB.

In this project, I converted a set of sentences into embeddings, stored them in ChromaDB, and experimented with retrieving similar sentences based on user queries.

This helped me understand how vector databases work and why they are important in RAG applications.

## What I Worked On

- Generated text embeddings using the Gemini Embedding API.
- Created a collection in ChromaDB to store the embeddings.
- Stored original sentences along with their embeddings and metadata.
- Implemented similarity search to retrieve the top matching sentences.
- Experimented with metadata filtering to retrieve results from specific categories.
- Used persistent storage to retain the stored data locally.

## Technologies Used

- Python
- Google Gemini Embedding API
- ChromaDB
- Google Gen AI SDK
- python-dotenv

## How It Works

1. Started with a collection of sample sentences related to programming, AI, and food.
2. Used Gemini to convert each sentence into a numerical representation called an embedding.
3. Stored the sentences, embeddings, IDs, and categories in a ChromaDB collection.
4. Provided a user query and generated an embedding for it using the same Gemini embedding model.
5. Used ChromaDB to find the three closest matching sentences.
6. Applied metadata filters to retrieve sentences from specific categories.

## Example

**User Query:**

"Tell me about machine learning."

The application converts the query into an embedding and searches the stored vectors in ChromaDB to retrieve the most relevant sentences.

I also tried filtering the results using categories such as `AI` and `Programming`.

## Project Structure

```text
ChromaDB/
│
├── main.py
├── requirements.txt
├── .gitignore
├── .env
└── chroma_db/
```

## How to Run

**1. Clone the repository**

```bash
git clone https://github.com/archna-v/chromadb-vector-search.git
```

**2. Navigate to the project folder**

```bash
cd chromadb-vector-search
```

**3. Install the required packages**

```bash
pip install -r requirements.txt
```

**4. Add your Gemini API key**

Create a `.env` file and add:

```env
GEMINI_API_KEY=your_api_key
```

**5. Run the project**

```bash
python main.py
```

## What I Learned

Working on this project gave me a better understanding of:

- How text is converted into embeddings.
- How vector databases store embeddings.
- How ChromaDB collections work.
- How similarity search retrieves relevant information.
- How metadata can be used to filter search results.
- How vector search fits into the retrieval stage of a RAG application.

This project is one of my hands-on steps towards learning and building LLM and RAG-based applications.

---

**Created by:** Archna V

**GitHub:** [archna-v](https://github.com/archna-v)
