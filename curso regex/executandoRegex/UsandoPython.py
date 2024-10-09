import re
text = "Jeferson Garcia"
pattern = r'(?P<name>[a-zA-Z]+)(?P<subname>\s[a-zA-Z]+)'
match = re.search(pattern, text)
print(match.group('subname'))  # Retorna 'abc\ndef'