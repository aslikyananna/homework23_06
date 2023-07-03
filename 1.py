list0 = [-1, 1, 2]
list1 = [2, 79, 4, 5]
list0 = list0 + list1
list_new = []
def merge (list0, list1):
    while len(list0) > 0:
        list_new.append(min(list0))
        list0.remove(min(list0))
        continue

print(merge())




