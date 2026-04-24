# tests/test_main.py

from src.config import DEBUG, DATABASE_URL

def test_debug_est_false():
    assert DEBUG == False   # doit être False en CI

def test_database_url_definie():
    assert DATABASE_URL is not None
