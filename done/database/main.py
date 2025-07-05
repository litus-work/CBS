
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os
load_dotenv()
connect = psycopg2.connect(
    host=os.environ.get("DB_HOST"),
    database=os.environ.get("DB_NAME"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    port=os.environ.get("DB_PORT"),
)

cursor = connect.cursor(cursor_factory=RealDictCursor)
connect.autocommit = True

def create_table_users():
    query = '''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INTEGER,
        gender VARCHAR(100) UNIQUE NOT NULL,
        nationality VARCHAR(100) UNIQUE NOT NULL
    );
    '''
    cursor.execute(query)

def create_table_posts():
    query = '''
    CREATE TABLE IF NOT EXISTS posts (
        id SERIAL PRIMARY KEY,
        user_id INTEGER,
        title VARCHAR(100) NOT NULL,
        description VARCHAR(100) UNIQUE NOT NULL
    );
    '''
    cursor.execute(query)

def create_table_comments():
    query = '''
    CREATE TABLE IF NOT EXISTS comments (
        id SERIAL PRIMARY KEY,
        user_id INTEGER,
        post_id INTEGER,
        text VARCHAR(100) NOT NULL
        
    );
    '''
    cursor.execute(query)

def create_table_emails():
    query = '''
    CREATE TABLE IF NOT EXISTS emails (
        id SERIAL PRIMARY KEY,
        user_id INTEGER,
        email VARCHAR(100) NOT NULL
        
    );
    '''
    cursor.execute(query)


def create_table_likes():
    query = '''
    CREATE TABLE IF NOT EXISTS likes (
        id SERIAL PRIMARY KEY,
        user_id INTEGER,
        post_id INTEGER
        
    );
    '''
    cursor.execute(query)


create_table_users()
create_table_posts()
create_table_comments()
create_table_emails()
create_table_likes()