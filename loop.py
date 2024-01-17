names = ["helo","guy","welcome"]
for name in names:
    print(name)

object_test = {"name":"hello","number" : 5,"arr" : ["one","two"]}

for val in object_test.values():
    print(val)

for key,val in object_test.items():
    print(key,"=>",val)

# nested loop 
values = ["one","two","three"]
for val1 in names:
    for val2 in values:
        print(val1,"is",val2)