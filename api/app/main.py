from fastapi import FastAPI

app = FastAPI(title="Mercado Vecino API")

@app.get("/health")
def health():
    return {"estado": "ok"}

@app.get("/tiendas")
def listar_tiendas():
    return [
        {"id": 1, "nombre": "Tienda Don Pedro", "barrio": "Suba"},
        {"id": 2, "nombre": "Minitienda Doña Maria", "barrio": "Teusaquillo"}
    ]