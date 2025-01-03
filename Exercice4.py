def merge_sorted_list(l1,l2):
    l = l1+l2
    return sorted(l)
l1=[1,7,3]
l2=[4,9,6]

print(merge_sorted_list(l1,l2))