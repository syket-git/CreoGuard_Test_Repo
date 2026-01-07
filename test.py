# Vulnerable Code for Testing CreoGuard

import pickle
import subprocess
import hashlib
import os

# ===== HARDCODED SECRETS =====
password = "admin123"
api_key = "sk-secret-key-12345"
db_password = "root123"
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"
JWT_SECRET = "super-secret-jwt-key"
DATABASE_URL = "postgresql://admin:password123@localhost/mydb"

# ===== SQL INJECTION =====
def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + user_id
    return query

def login(username, password):
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    return query

def search_users(name):
    query = "SELECT * FROM users WHERE name LIKE '%" + name + "%'"
    return query

# ===== COMMAND INJECTION =====
def ping_server(host):
    os.system("ping -c 1 " + host)

def run_command(cmd):
    subprocess.call(cmd, shell=True)

def list_files(directory):
    os.popen("ls " + directory)

# ===== DANGEROUS FUNCTIONS =====
eval(input("Enter command: "))

def execute_code(code_string):
    exec(code_string)

# ===== INSECURE DESERIALIZATION =====
def load_data(user_input):
    return pickle.loads(user_input)

# ===== WEAK CRYPTOGRAPHY =====
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def encrypt_data(data):
    return hashlib.sha1(data.encode()).hexdigest()

# ===== PATH TRAVERSAL =====
def read_file(filename):
    with open("/var/www/uploads/" + filename, "r") as f:
        return f.read()

def download_file(user_path):
    return open(user_path).read()

# ===== XSS VULNERABILITIES =====
def render_html(user_input):
    return f"<div>{user_input}</div>"

def create_link(url):
    return f'<a href="{url}">Click here</a>'

# ===== INSECURE RANDOM =====
import random
def generate_token():
    return random.randint(100000, 999999)

def generate_session_id():
    return str(random.random())

# ===== HARDCODED IP/URLS =====
API_ENDPOINT = "http://192.168.1.100:8080/api"
DEBUG_MODE = True
ADMIN_EMAIL = "admin@company.com"
