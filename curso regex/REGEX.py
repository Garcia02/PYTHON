import re
text = "Isso é incrível! tudo mais!"
pattern =  r'[^?.!].*!'
match = re.findall(pattern,text,re.MULTILINE)
print (match) 
