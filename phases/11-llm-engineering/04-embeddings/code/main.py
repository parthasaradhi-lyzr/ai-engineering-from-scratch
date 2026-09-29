from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("OPENROUTER_API_KEY"))
print(os.getenv("BASE_URL"))
openai = OpenAI(api_key=os.getenv("OPENROUTER_API_KEY"),base_url=os.getenv("BASE_URL"))

def chunking(text,chunk_size=500,overlap_size=50):
    chunks = [text[0:chunk_size]]
    for i in range(chunk_size-overlap_size, len(text), chunk_size-overlap_size):
        chunks.append(text[i:i+chunk_size])
    return chunks

def embedding(text,model="liquid/lfm-2.5-embedding-350m:free"):
    import openai
    response = openai.embeddings.create(
        input=text,
        model=model
    )
    return response.data[0].embedding

def main():
    text = "This is a sample text that we will use to demonstrate chunking and embedding. " * 20
    chunks = chunking(text)
    embeddings = [embedding(chunk) for chunk in chunks]
    print(f"Number of chunks: {len(chunks)}")
    print(f"Embedding of first chunk: {embeddings[0]}")

main()
