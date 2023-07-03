def is_sortedde(x):
    for i in range(len(x)):
        if x[i] < x[i+1] or x[i] == x[i+1]:
            return True
        else:
            return False
sort = is_sortedde([8,8,8,9])
print(sort)

