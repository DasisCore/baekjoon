data = input().upper()
search = list(set(data))


countarr = []
for i in search:
    countarr.append(data.count(i))

if countarr.count(max(countarr)) > 1:
    print("?")
else:
    print(search[countarr.index(max(countarr))])