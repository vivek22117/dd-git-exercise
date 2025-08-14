def find_common_elements(list_a,list_b):
    set_a=set()
    for i in list_a:
        if i in list_b:
            set_a.add(i)
    return set_a

list_a = [1, 2, 3, 4, 5, 1, 4]
list_b = [4, 5, 6, 7, 8, 5]
common = find_common_elements(list_a, list_b)
print(f"List A: {list_a}")
print(f"List B: {list_b}")
print(f"Common Elements: {common}")


