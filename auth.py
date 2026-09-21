def verify_token(token: str) -> bool:
    """Validate bearer token."""
    if not token:
        return False
    return token.startswith("Bearer ")
