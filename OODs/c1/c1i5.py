'''จงสร้าง vickrey auction แบบจำลอง
Vickrey auction คือการประมวลที่ผู้ที่จะชนะการประมูล คือ ผู้ที่ยื่นซองเสนอราคาสูงที่สุด แต่จะจ่ายจริงในราคาที่สูงเป็นอันดับสองรองลงมา
word'''
"Enter All Bid : "
"not enough bidder"
"error : have more than one highest bid"
"winner bid is $ need to pay $"""

bidder = [int(e) for e in input("Enter All Bid : ").split()]
bidder.sort()
if len(bidder) == 1:
    print("not enough bidder")
else:
    if bidder[-1] == bidder[-2]:
        print("error : have more than one highest bid")
    else:
        print("winner bid is %d need to pay %d"% (bidder[-1], bidder[-2]))