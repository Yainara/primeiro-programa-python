import sqlite3
from sqlite3 import Error
from models.Pessoa import Pessoa

database = r"pythonsqlite.db"

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def find(name: str):
    conn = create_connection(database)

    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = ?", (name, ))

    rows = cur.fetchall()

    conn.close()

    return rows

def insert(pessoa: Pessoa):
    try:
        conn = create_connection(database)

        sql = ''' INSERT INTO users(name, email, address, city, state, cep)
                  VALUES(?,?,?,?,?,?) '''

        cur = conn.cursor()
        cur.execute(sql, (pessoa.name, pessoa.email, pessoa.address, pessoa.city, pessoa.state, pessoa.cep,))
        conn.commit()
        return cur.lastrowid
    except Exception as e:
        print(type(e))
        raise

def edit(pessoa: Pessoa):
     try:
         conn = create_connection(database)

         sql = ''' UPDATE users
                   SET email = ?, address = ?, city = ?, state = ?, cep = ?
                   WHERE name = ?
                '''

         cur = conn.cursor()
         cur.execute(sql, ( pessoa.email, pessoa.address, pessoa.city, pessoa.state, pessoa.cep, pessoa.name))
         conn.commit()
         return cur.lastrowid
     except Exception as e:
         print(type(e))
         raise

def deletar(pessoa: Pessoa):
  try:
      conn = create_connection(database)

      sql = "DELETE FROM users WHERE name=?"

      cur = conn.cursor()
      name = pessoa.name
      cur.execute(sql, (name,))
      conn.commit()
      return cur.lastrowid
  except Exception as e:
      print(type(e))
      raise
