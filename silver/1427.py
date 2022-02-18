# 1427. 소트인사이드

n = input()

li = []
for i in n:
    li.append(i)

li.sort(reverse=True)
print("".join(li))