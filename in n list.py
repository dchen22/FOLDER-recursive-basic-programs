def in_nlist(list, target):
    found = False
    for i in list:
        if i == target:
            return True
        elif type(i) == type(list):
            found = in_nlist(i, target)
    return found


print(in_nlist([4, [3], [4, 6, 7], 4], 5))