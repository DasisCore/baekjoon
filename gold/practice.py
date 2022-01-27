# 1662. 압축
def lonely(a):
    li = []
    li.append(a[0])
    for i in range(1, len(a)): 
        if a[i] != a[i-1]: #리스트 안의 가장 최근에 넣었던 문자와 다르면,
            li.append(a[i])
    return li

print(lonely([1, 1, 3, 3, 0, 1, 1]))
print(lonely([4, 4, 4, 3, 3]))