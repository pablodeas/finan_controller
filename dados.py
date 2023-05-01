# O jeito é ir de MySql mesmo
import mysql.connector

# BANCO DE DADOS DESTE PROJETO SE CHAMA (finan_db)

# Abrindo conexão com database local / Só possível com xampp ligado
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "2656",
    database = "finan_db"
)

#   Criando o cursor, o que executa os comandos
dbcursor = db.cursor()


