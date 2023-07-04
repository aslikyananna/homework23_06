def is_sortedde(x):
    for i in range(len(x)):
        if x[i] < x[i+1]:
            return True
        else:
            return False
sort = is_sortedde([8,8,4,9,7])
print(sort)
