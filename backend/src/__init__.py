import os

from flask import Flask, jsonify
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv
from sqlalchemy import text, create_engine
from sqlalchemy.exc import ProgrammingError

from config import DevelopmentConfig, TestingConfig, ProductionConfig

load_dotenv()
app = Flask(__name__)
CORS(app)

if os.getenv('APP_ENV').lower() == 'development':
    app_settings = DevelopmentConfig
    app.config.from_object(app_settings)
elif os.getenv('APP_ENV').lower() == 'testing':
    app_settings = TestingConfig
    app.config.from_object(app_settings)
elif os.getenv('APP_ENV').lower() == 'production':
    app_settings = ProductionConfig
    app.config.from_object(app_settings)
else:
    app_settings = DevelopmentConfig
    app.config.from_object(app_settings)





# Configuration for the 'postgres' default database
DEFAULT_DATABASE_URL = "postgresql://postgres:postgres@localhost/postgres"
TARGET_DATABASE_URL = "postgresql://postgres:postgres@localhost/ejada"

# Create an engine connected to the default database
default_engine = create_engine(DEFAULT_DATABASE_URL)

# Check if the target database exists
db_exists_query = text("SELECT 1 FROM pg_database WHERE datname='ejada'")
conn = default_engine.connect()
db_exists = conn.execute(db_exists_query).scalar()
conn.close()

if not db_exists:
    import psycopg2
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

    # Configuration for the 'postgres' default database
    DEFAULT_DATABASE_URL = "dbname=postgres user=postgres password=postgres host=localhost"

    try:
        # Connect to the default database
        conn = psycopg2.connect(DEFAULT_DATABASE_URL)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        # Create a cursor to perform database operations
        cur = conn.cursor()

        # Execute the CREATE DATABASE command
        cur.execute('CREATE DATABASE ejada')
        cur.close()  # Close the cursor
        print("Database 'ejada' created successfully.")
    except Exception as e:
        print(f"An error occurred while creating the database: {e}")
    finally:
        if conn:
            conn.close()  # Close the connection
else:
    print("Database 'ejada' already exists.")





# set default database url
app.config['SQLALCHEMY_DATABASE_URI'] = TARGET_DATABASE_URL
# create database tables

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)




