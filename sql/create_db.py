import sqlite3

def main():
    conn = sqlite3.connect("db.sql")
    cur = conn.cursor()

    command = "CREATE TABLE user_data(last_path TEXT, format VARCHAR(10))"


if __name__ == '__main__':
    main()