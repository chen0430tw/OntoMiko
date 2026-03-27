"""
Pytest configuration and fixtures
"""

import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI application"""
    return TestClient(app)


@pytest.fixture
def sample_text():
    """Sample text for testing"""
    return "未来是否存在依靠潜势和惯性计算的通用拟构处理器？"
