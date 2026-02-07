import os
import json

ACCOUNTS_DIR = "accounts"
os.makedirs(ACCOUNTS_DIR, exist_ok=True)

def list_accounts():
    return os.listdir(ACCOUNTS_DIR)

def save_account(username, storage_state):
    path = f"{ACCOUNTS_DIR}/{username}"
    os.makedirs(path, exist_ok=True)

    with open(f"{path}/storage_state.json", "w") as f:
        json.dump(storage_state, f)

def account_exists(username):
    return os.path.exists(f"{ACCOUNTS_DIR}/{username}")
