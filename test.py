# Bad code example for testing
password = "admin123"  # hardcoded password
api_key = "sk-secret-key-12345"

def get_user(id):
    query = "SELECT * FROM users WHERE id = " + id  # SQL injection
    return query

eval(input("Enter code: "))  # dangerous eval
