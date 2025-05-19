from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import json
import os

app = FastAPI()

# 🔓 CORS liberado para React consumir
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_DIR = "backend/data"
STATIC_DIR = "backend/static"

@app.get("/dados")
def get_dados():
    df = pd.read_csv(os.path.join(DATA_DIR, "dados_renda_valida.csv"))
    return df.to_dict(orient="records")

@app.get("/metricas")
def get_metricas():
    with open(os.path.join(DATA_DIR, "metricas_modelos.json")) as f:
        return json.load(f)

@app.get("/rondonia")
def get_rondonia():
    df = pd.read_csv(os.path.join(DATA_DIR, "estatisticas_rondonia.csv"))
    return df.to_dict(orient="records")