'''โจทย์: จงเขียนโปรแกรมรับความเร็วลมเฉลี่ยใน 10 นาที และแสดงผลระดับพายุที่เกิดขึ้น จากการจัดแบ่งความเร็วลมดังนี้

		Speed (km/h)		ระดับพายุ
			0-51.99			Breeze
			52.00-55.99		Depression
			56.00-101.99	        Tropical Storm
			102.00-208.99	        Typhoon
			>= 209			Super Typhoon

โดยแสดงผลตามตัวอย่างการแสดงผล'''
print(" *** Wind classification ***")
windSpeed = float(input("Enter wind speed (km/h) : "))
if (windSpeed>=0 and windSpeed <= 51.9):
    print("Wind classification is Breeze.")
elif (windSpeed>=52 and windSpeed <= 55.9):
    print("Wind classification is Depression.")
elif(windSpeed>=56.00 and windSpeed <= 101.99):
    print("Wind classification is Tropical Storm.")
elif(windSpeed>=102.00 and windSpeed <= 208.99):
    print("Wind classification is Typhoon.")
elif(windSpeed>=209.00):
    print("Wind classification is Super Typhoon.")