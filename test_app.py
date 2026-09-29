from app import app


def test_home_page():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert b"Shanif M" in r.data