'''รับจำนวนเต็ม 3 จำนวนจากแป้นพิมพ์
เก็บในตัวแปร h, m และ s ซึ่งแทนจำนวน ชั่วโมง นาที และ วินาที

แล้วแสดงผลเป็น วินาที
แสดงผลตามตัวอย่าง'''
print("*** Converting hh.mm.ss to seconds ***")

h, m, s = [int(x) for x in input("Enter hh mm ss : ").split()]

# check all correct
if (h >= 0) and (m >= 0 and m <= 59) and (s >= 0 and s <= 59):
    result = "{:,}".format(((h*3600)+(m*60)+s))
    if h < 10 and m < 10 and s < 10:
        print("0" + str(h) + ":"+"0" + str(m) + ":" + "0" +
              str(s) + " = " + str(result) + " seconds")
    elif h < 10 and m > 10 and s > 10:
        print("0" + str(h) + ":" + str(m) + ":" +
              str(s) + " = " + str(result) + " seconds")
    elif m < 10 and h > 10 and s > 10:
        print("0" + str(h) + ":"+"0" + str(m) + ":" +
              str(s) + " = " + str(result) + " seconds")
    elif s < 10 and m > 10 and h > 10:
        print("0" + str(h) + ":" + str(m) + ":" +
              str(s) + " = " + str(result) + " seconds")
    else:
        print(str(h) + ":" + str(m) + ":" + str(s) +
              " = " + str(result) + " seconds")

# check minute incorrect!
elif (h >= 0) and (m < 0 or m >= 59) and (s >= 0 or s <= 59):
    print("mm(" + str(m) + ")" + " is invalid!")
