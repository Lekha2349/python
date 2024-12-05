#various datatypes
str = "sri lekha"
print(str)
age = 19
print(int)
weight = 45.5
print(float)
is_veg = False
print(is_veg)
# typecasting
print(int(weight))
print(int(is_veg))
list= ["vinay","lekha","satwi"]
print(list)
list.append("abhi")
print(list)
list.insert(2,"ammu")
print(list)
list.remove("vinay")
print(list)
list.sort()
print(list)
list.reverse()
print(list)
#tuple
tup=("anu",1,"lekha")
print(tup)
#count
count= tup.count("lekha")
print(count)
#index
index = tup.index("anu")
print(index)
nested_tup=(("anu",1,"lekha"),("virat","rohit","gill"))
print(nested_tup)
#set
set={1,"munni","virat",7}
print(set)
#dictionary
dict={"name":"lekha","age":19,"city":"bhimavaram"}
print(dict)

value=dict.get("name")
print(value)
#items
items=dict.items()
print(items)
#pop
value=dict.pop("age")
print(value)
print(dict)

            


