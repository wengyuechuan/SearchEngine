import re

string = "1.abc2.acs3.hhh"
result = re.findall(r'(?:\d+\.)?([a-zA-Z]+)', string)
print(result)
