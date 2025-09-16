import re
from pathlib import Path
from fastapi import FastAPI
from pypdf import PdfReader
from fastapi import FastAPI, HTTPException

app = FastAPI()

PASTA_RAIZ = Path(__file__).parent.parent
caminho_arquivo_pdf = PASTA_RAIZ / "data" / "Boletim - 202508011-BOL2250269206646538130.pdf"

leitor_pdf = PdfReader(caminho_arquivo_pdf)
primeira_pagina = leitor_pdf.pages[0]
texto_do_pdf = primeira_pagina.extract_text()

dados_praias = []
linhas = texto_do_pdf.split('\n')
for linha in linhas:
    match = re.match(r'^(\d+)[LCO]\s*-\s*(.*)', linha)
    if match:
        praia_id = int(match.group(1))
        nome_praia = match.group(2).strip()
        status = "Própria" if linha.strip().endswith('P') else "Imprópria"
        dados_praias.append({
            "id": praia_id,
            "nome": nome_praia,
            "status": status
        })

@app.get("/")
def ler_raiz():
    return {"message": "Bem-vindo à API de Balneabilidade!"}

@app.get("/praias")
def listar_praias_do_pdf():
    return dados_praias

@app.get("/praias/{praia_id}")
def buscar_praia_por_id(praia_id: int):
    for praia in dados_praias:
        if praia.get("id") == praia_id:
            return praia
    raise HTTPException(status_code=404, detail="Praia com o ID informado não foi encontrada.")