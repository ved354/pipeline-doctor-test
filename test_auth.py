# Developer accidentally imports non-existent validate_token
from auth import validate_token

def test_verify_token_valid():
    assert validate_token("Bearer secret-123") is True
