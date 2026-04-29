from openai import OpenAI
import os
import json
import random
from dotenv import load_dotenv


load_dotenv()

def embedding(*, client, content:str):
  try:
    text = content.replace("\n", " ")

    response = client.embeddings.create(
      model='text-embedding-3-small',
      input=text
    )
    return response.data[0].embedding
  
  except Exception as e:
    print(f"Error retrieving embedding: {e}")
    return None
  
def getEmbeddingOpenAI(content:str):
  client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
  result = embedding(client=client, content=content)

  return json.dumps(result)


def get_dummy_embedding():
    """
    Menghasilkan dummy vector 1536 dimensi 
    untuk simulasi model text-embedding-3-small
    """
    # Menghasilkan 1536 angka acak antara -1 dan 1
    dummy_list = [random.uniform(-1, 1) for _ in range(1536)]
    
    # Langsung kembalikan dalam format STRING agar siap untuk SQL CAST
    return json.dumps(dummy_list)

# --- CARA PAKAI DI NOTEBOOK ---

# Gantinya manggil OpenAI, panggil ini:
embedding_data = get_dummy_embedding()

print(f"Tipe Data: {type(embedding_data)}")
print(f"Panjang Karakter: {len(embedding_data)}")
print(f"Preview: {embedding_data[:100]}...")