def revList(alist):
    if len(alist) == 1:       
        return alist #base case
    else:
        return revList(alist[1:]) + [alist[0]]

inp = revList(sorted([int(i) for i in input("Enter your List : ").split(",")]))

print("List after Sorted :",inp)