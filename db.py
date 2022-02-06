import os

import psycopg2 as psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    """コネクションを貼る関数"""
    dsn = os.environ.get("DATABASE_URL")
    return psycopg2.connect(dsn)


def init_db():
    """データベースの初期化を行う関数"""
    with get_connection() as conn:
        with conn.cursor() as cur:
            with open('schema.sql', encoding="utf-8") as f:
                cur.execute(f.read())


if __name__ == '__main__':
    init_db()
