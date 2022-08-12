'''
จงเขียนฟังก์ชันเพื่อหาผลรวมของ 3 พจน์ใดๆใน Array ที่มีผลรวมเท่ากับ 0 สำหรับ Array ที่มีข้อมูลข้างในเป็นจำนวนจริง ***Array ต้องมีความยาวตั้งแต่ 3 จำนวนขึ้นไป***
'''

from itertools import combinations
ans = [int(x) for x in input("Enter Your List : ").split()]
if len(ans) < 3:
    print("Array Input Length Must More Than 2")
    quit()
trueAns = []
for x in combinations(ans, 3):
    if sum(x) == 0 and sorted(x) not in trueAns:
        trueAns.append(sorted(x))

print(trueAns)