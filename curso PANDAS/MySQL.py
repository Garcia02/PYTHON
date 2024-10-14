import mysql.connector
import pandas as pd

# Conectar ao servidor MySQL sem especificar um banco de dados
conexao = mysql.connector.connect(
    host="127.0.0.1",  # Substitua pelo seu host, se necessário
    user="root",  # Substitua pelo seu usuário
    password=""  # Substitua pela sua senha
)

cursor = conexao.cursor()

cursor.execute("USE new_schema")
cursor.execute("UPDATE clientes SET Nome = 'Jefinho' WHERE Nome = 'Jeferson Garcia'")

# Consumir todos os resultados da consulta
#resultados = cursor.fetchall()

# Obter os nomes das colunas
#colunas = [desc[0] for desc in cursor.description]

# Criar um DataFrame do pandas com os resultados
#df = pd.DataFrame(resultados, columns=colunas)

# Exibir o DataFrame
#print(df)

conexao.commit()

# Fechar o cursor e a conexão
cursor.close()
conexao.close()