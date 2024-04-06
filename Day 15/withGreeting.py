import time

currentTime = time.strftime("Current Time :- %H:%M:%S")
print(currentTime)

name = input("Enter Your Name :- ")

hour = int(time.strftime("%H"))
minutes = int(time.strftime("%M"))
nowTime = time.strftime('%H:%M:%S')

# GREETING CONDITIONS
if(4<=hour<=11 and 00<=minutes<=59):
    print("Hi, ", name,"\nGOOD MORNING its", nowTime,"AM")
elif(12<=hour<=17):
    print("What's up ", name,"\nGOOD AFTERNOON its", nowTime,"PM")
elif(17<=hour<=19):
    print("Hello, ", name,"\nGOOD EVENING its", nowTime,"PM")
else:
    print("GOOD NIGHT ", name," its", nowTime,"PM")
