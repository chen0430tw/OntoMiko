"""
API tests for OntoMiko backend
"""

from conftest import client, sample_text


def test_health(client):
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_divine_text_basic(client, sample_text):
    """Test basic text divination"""
    response = client.post(
        "/divine/text",
        json={"text": sample_text}
    )
    assert response.status_code == 200
    data = response.json()
    assert "category" in data
    assert "state" in data
    assert "reason" in data


def test_divine_text_empty(client):
    """Test with empty text"""
    response = client.post(
        "/divine/text",
        json={"text": ""}
    )
    assert response.status_code == 200


def test_divine_text_pmm_detection(client):
    """Test PMM (perpetual motion) detection"""
    response = client.post(
        "/divine/text",
        json={"text": "永动机能否实现？"}
    )
    assert response.status_code == 200
    data = response.json()
    # Should detect PMM context
    assert "pmm" in data


def test_divine_text_consistency_check(client):
    """Test consistency check"""
    response = client.post(
        "/divine/text",
        json={"text": "一个自相矛盾的设想"}
    )
    assert response.status_code == 200
    data = response.json()
    # Should detect inconsistency
    assert "category" in data
