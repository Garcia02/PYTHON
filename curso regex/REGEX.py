import re
text = "Visite nosso site em https://www.exemplo.com para mais detalhes"
pattern =  r'https?://(?:www\.)?([\w-]+\.\w{2,3})'
match = re.findall(pattern,text)
print (match) 
