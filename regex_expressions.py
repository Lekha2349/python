# regex expression is a special sequence of characters that uses a search pattern to find a string or set of strings
# various functions we use
# match
# findall
# split
# sub
# search
import re
a="my name is perry, my age is 30"
b=re.match("my",a)
print(b)
import re
a="i like biriyani, i hate sweets"
b=re.search("i",a)
print(b)
import re
a="my name is perry, i like sweets"
b=re.split("perry",a)
print(b)
import re
a="my name is virat, i like cricket"
b=re.sub("virat","kohli",a)
print(b)