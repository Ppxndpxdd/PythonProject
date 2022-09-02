
def revList(alist):
    if len(alist) == 1:
        return alist  # base case
    else:
        return revList(alist[1:]) + [alist[0]]


inp = input("Enter your List : ").split(",")
inp = list(map(int,inp))
print(inp)
print("List after Sorted : " + "[" + ", ".join(revList(sorted(inp)))+"]")

# n = []
# for i in inp:
#     if i < 0:
#         n+=i
#  if inp[0] < 0:
#      print("List after Sorted : " + "[" + ", ".join(sorted(inp))+"]")
#  else:
#      print("List after Sorted : " + "[" + ", ".join(revList(sorted(inp)))+"]")
