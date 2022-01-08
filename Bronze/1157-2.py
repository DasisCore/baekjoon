data = input().upper()
search = list(set(data))

array = []
for i in search:
    array.append(data.count(i))

if array.count(max(array)) > 1:
    print("?")
else:
    print(search[array.index(max(array))])
    print(max(array))