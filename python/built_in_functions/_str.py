"""создает новый str-объект. В текстовом виде можно представить все типы объектов, но для них используется repr"""

s1 = str(517)
s2 = str([1, 2, 3, 4])
s3 = str(range(6))

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))