import sqlite3

def main():
    db = sqlite3.connect('02/test.db')
    cur = db.cursor()
    
    cur.execute("CREATE TABLE users(name STRING(50))")
    cur.execute("INSERT INTO users (name) VALUES ('navid')")
    db.commit()

    users = cur.execute("SELECT * FROM users")
    for i, user in enumerate(users):
        print(f'user {i + 1} name is: {user[0]}')
    db.close()

if __name__ == "__main__":
    main()