# Bad code for testing CreoGuard

password = "admin123"
api_key = "sk-secret-key-12345"
db_password = "root123"

def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return query

def login(username, password):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    return query

eval(input("Enter command: "))

import pickle
data = pickle.loads(user_input)
