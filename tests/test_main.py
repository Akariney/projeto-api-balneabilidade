from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_listar_praias_retorna_status_200():
    response = client.get("/praias")
    assert response.status_code == 200

def test_listar_praias_retorna_uma_lista():
    response = client.get("/praias")
    assert isinstance(response.json(), list)

def test_formato_do_item_da_lista():
    response = client.get("/praias")
    data = response.json()
    assert len(data) > 0
    primeiro_item = data[0]
    assert "id" in primeiro_item
    assert "nome" in primeiro_item
    assert "status" in primeiro_item

def test_buscar_praia_por_id_existente():
    response = client.get("/praias/13")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 13

def test_buscar_praia_por_id_inexistente():
    response = client.get("/praias/999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Praia com o ID informado não foi encontrada."