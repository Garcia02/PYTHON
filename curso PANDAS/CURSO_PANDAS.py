import pandas as pd

# DataFrame simples
df = pd.DataFrame({
    'nome': ['Ana', 'Bruno', 'Carla', 'Daniel'],
    'idade': [25, 32, 28, 41],
    'cidade': ['SP', 'RJ', 'SP', 'MG']
})

print(df)