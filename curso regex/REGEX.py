import re
text = "line1\n\nline2\n\n\nline3"
pattern =  r'^\s*$'
match = re.search(pattern,text,re.MULTILINE)
print (match.group()) 
