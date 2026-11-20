import chromadb
from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

gemini_client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

client = chromadb.PersistentClient(
    path="./chroma_db"
)

print("ChromaDB connected successfully!")

collection = client.get_or_create_collection(
    name="my_sentences"
)

print("Collection created successfully!")

sentences = [
    "Python is a programming language.",
    "Java is used for software development.",
    "Machine learning helps computers learn.",
    "Deep learning uses neural networks.",
    "I love eating pizza."
]

def get_embedding(text):

    response = gemini_client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )

    embedding = response.embeddings[0].values

    return embedding
embeddings = []

for sentence in sentences:

    embedding = get_embedding(sentence)

    embeddings.append(embedding)

print("Total embeddings:", len(embeddings))
print("Dimensions:", len(embeddings[0]))

collection.upsert(

    ids=["1", "2", "3", "4", "5"],

    documents=sentences,

    embeddings=embeddings,

    metadatas=[
        {"category": "Programming"},
        {"category": "Programming"},
        {"category": "AI"},
        {"category": "AI"},
        {"category": "Food"}
    ]
)

print("Embeddings stored successfully!")
print("Total records:", collection.count())

query = "Tell me about machine learning."

query_embedding = get_embedding(query)

results = collection.query(
    query_embeddings=[query_embedding],
    n_results=3
)

for i in range(len(results["documents"][0])):

    print("Document:", results["documents"][0][i])

    print("Metadata:", results["metadatas"][0][i])

    print("Distance:", results["distances"][0][i])

    print("-------------------")

