from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

# Configurando a chave de API OpenAI (substitua pela sua) pegar do .env
openai.api_key = os.getenv("OPENAI_API_KEY")

# Definindo o modelo FastAPI
app = FastAPI()

# Criando um modelo Pydantic para as entradas da API
class Query(BaseModel):
    prompt: str
    max_tokens: int = 100

# Definindo a rota de API para responder perguntas usando GPT-3
@app.post("/ask")
async def ask_gpt3(query: Query):
    response = openai.Completion.create(
      engine="text-davinci-002", # você pode usar outros modelos também, depende da sua necessidade
      prompt=query.prompt,
      max_tokens=query.max_tokens
    )
    return response.choices[0].text.strip()
