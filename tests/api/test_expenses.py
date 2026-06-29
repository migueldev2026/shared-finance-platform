from shared_finance import create_app


def test_get_expenses():

    app = create_app()

    client = app.test_client()

    response = client.get("/expenses")

    assert response.status_code == 200

    data = response.get_json()

    assert len(data) == 2

    assert data[0]["category"] == "Mercado"

    assert data[1]["paid_by"] == "Laura"