import pandas as pd

# DataFrame simples
df = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carla', 'Daniel'],
    'idade': [25, 32, 28, 41],
    'cidade': ['SP', 'RJ', 'SP', 'MG']
})

print(df)

# Todos têm mais de 20 anos?
todos_mais_20 = (df['idade'] > 20).all()
print(f"\nTodos têm mais de 20 anos? {todos_mais_20}")