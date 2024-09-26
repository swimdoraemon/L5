usage = int(input("enter your electricty usage"))

if usage <= 50:
  usage = (usage*2.6)+25
elif usage <= 100:
  usage = (usage*3.25)+35
else:
  usage = (usage*5.26)+45

print ("your elctrictity bill is ",usage)