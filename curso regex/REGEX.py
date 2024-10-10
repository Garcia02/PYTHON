import re
text = "Isso é incrível! , isso é maravilho! sim, isso é muito marivilho."
pattern =  r'[^?.!].*!'
match = re.findall(pattern,text)
print (match) 
