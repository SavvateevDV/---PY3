list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]
uniclist=[]
median=0
for number in list_:
    if number not in uniclist:
        median+=number
        uniclist.append(number)
print(sum(uniclist))
print(len(uniclist))
print(round(median/len(uniclist),5))
#пустая строка