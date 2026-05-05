from openai import OpenAI
import os
import json
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