from flask import Flask
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    #conexão com o bd MySql
    
    return mysql.connector.connect(
        host='bd', #nome do bd no docker
        user='root',
        password='exampe',
        daabase='biblioteca'
    )

@app.route('/')
def home():
    #liga aao bd e faz consulta simples
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros;')
    livros = cursor.fetchall()
    cursos.close()
    conn.close()
    
    #cria ums string HTML para mostrar os resultados
    utput = "<h1>Livros na Biblioteca</h1><ul>"
    for livro in livros:
        output += f"<li>{livro[0]} - {livro[1]} - {livro[2]}</li>"
    output += "</ul>"
    
    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    