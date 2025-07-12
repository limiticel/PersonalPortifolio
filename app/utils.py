import random 
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, '../data/storage.json')

def generate_random_string():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return ''.join(random.choice(characters) for _ in range(10))

def load_data():
    with open(DATA_PATH, "r", encoding='utf-8') as f:
        return json.load(f)

def save_data(data):
    print("saving data")
    with open(DATA_PATH, "w", encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print("data saved successfully")
