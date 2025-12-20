import os
import ast

# Good code example - fixed version

# Use environment variables for secrets
password = os.getenv("APP_PASSWORD")
api_key = os.getenv("API_KEY")


def get_user(user_id: int) -> str:
    """Fetch user by ID using parameterized query."""
    # Use parameterized queries to prevent SQL injection
    query = "SELECT * FROM users WHERE id = %s"
    return query, (user_id,)


def safe_eval(user_input: str):
    """Safely evaluate user input using ast.literal_eval."""
    try:
        return ast.literal_eval(user_input)
    except (ValueError, SyntaxError):
        return None
