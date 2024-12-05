# sequence of characters #
#immutable#
i1="hello"
print(id(i1))

i1=i1+", world"
print(id(i1))
# string index and slicing#
s_1="python"

print(s_1[0:1]) # right side of the colon is exclusive. 0 and <1
print(s_1[0:2])
print(s_1[2:]) # inclusive#
print(s_1[:5])
s_method="i Am Learning python"
print(s_method.capitalize())
print(s_method.casefold())
p="Hello"
print(p== "hello")
print(s_method.endswith("python")) 
# srings concatenation#
# string formatting and escaping#
print(5*"python")
fs="\"\thello, world\""
print(fs)
py="python"
fs1=f"i am learning{py}"
print(fs1)
print("i am learning {}, from last{} week".format(py, 1))