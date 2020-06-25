import re

txt = "The rain in Spain and after the following, there is (7) another The Spain What wrong (8) what abou the rest (9)"
x = re.search(r"(Spain and).*?\(", txt)

print(x)
# if type(x) == 'None':
print(x.group(0))
