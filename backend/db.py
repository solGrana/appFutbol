import psycopg2
import os
from decouple import config

def get_connection():
    return psycopg2.connect(
        dbname=config("DB_NAME"),
        user=config("DB_USER"),
        password=config("DB_PASSWORD"),
        host=config("DB_HOST"),
        port=config("DB_PORT")
    )
