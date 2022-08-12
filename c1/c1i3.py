
'''โรงเรียนดังประจำจังหวัดแห่งหนึ่ง จะมีการจัดการเลือกตั้งหาประธานนักเรียนคนใหม่ขึ้นในทุกๆปี โดยในปีนี้มีผู้เข้าแข่งขันสูงถึง 20 คน โดยกฤษฎาได้รับมอบหมายให้เป็นผู้นับคะแนนเลือกตั้งในปีนี้ แต่กฤษฎารู้สึกขี้เกียจนับคะแนนขึ้นมา จึงได้ไหว้วานให้คุณช่วยเขียนโปรแกรม ในการหาว่าผู้เข้าแข่งขันคนใดได้รับคะแนนสูงที่สุด

ข้อควรระวัง หากมีการเลือกเลขที่ไม่ตรงกับผู้เข้าแข่งขัน (1-20) จะนับว่าเป็นบัตรเสีย และถ้าหากทุกใบเป็นบัตรเสียจะถือว่าไม่มีผู้ชนะ'''

import statistics

print("*** Election ***")
n = int(input("Enter a number of voter(s) : "))

votes = list(map(int,input().strip().split()))[:n] 

def most_frequent(List):
     for data in List[:]:
          if data <= 0 or data > 20:
               List.remove(data)
     if List == []:
          return "*** No Candidate Wins ***"
     else:
          return max(set(List), key = List.count) 
List = votes
print(most_frequent(List))