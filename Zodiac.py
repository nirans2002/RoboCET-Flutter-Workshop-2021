#Program to determine your zodiac sign
print("This is a Program to Determine your Zodiac Sign\n")
date = input("Enter your Date of Birth in DD-MM Format")
dd = int(date[:2])
mm = int(date[3:])
if(mm==1):
    if(dd<=20):
        print("You are CAPRICORN, the goat")
    elif(dd>20 and dd<=31):
        print("You are AQUARIUS, the water carrier")
    else:
        print("Invalid Input")

elif(mm==2):
    if(dd<=18):
        print("You are AQUARIUS, the water carrier")
    elif(dd>18 and dd<=29):
        print("You are PISCES, the fish")
    else:
        print("Invalid Input")

elif(mm==3):
    if(dd<=20):
        print("You are PISCES, the fish")
    elif(dd>20 and dd<=31):
        print("You are ARIES, the ram")
    else:
        print("Invalid Input")

elif(mm==4):
    if(dd<=20):
        print("You are ARIES, the ram")
    elif(dd>20 and dd<=30):
        print("You are TAURUS, the bull")
    else:
        print("Invalid Input")

elif(mm==5):
    if(dd<=21):
        print("You are TAURUS, the bull")
    elif(dd>21 and dd<=31):
        print("You are GEMINI, the twins")
    else:
        print("Invalid Input")

elif(mm==6):
    if(dd<=21):
        print("You are GEMINI, the twins")
    elif(dd>21 and dd<=30):
        print("You are CANCER, the crab")
    else:
        print("Invalid Input")

elif(mm==7):
    if(dd<=22):
        print("You are CANCER, the crab")
    elif(dd>22 and dd<=31):
        print("You are LEO, the lion")
    else:
        print("Invalid Input")

elif(mm==8):
    if(dd<=23):
        print("You are LEO, the lion")
    elif(dd>23 and dd<=31):
        print("You are VIRGO, the goddess")
    else:
        print("Invalid Input")

elif(mm==9):
    if(dd<=22):
        print("You are VIRGO, the goddess")
    elif(dd>22 and dd<=30):
        print("You are LIBRA, the scales")
    else:
        print("Invalid Input")

elif(mm==10):
    if(dd<=23):
        print("You are LIBRA, the scales")
    elif(dd>23 and dd<=31):
        print("You are SCORPIO, the scorpion")
    else:
        print("Invalid Input")

elif(mm==11):
    if(dd<=22):
        print("You are SCORPIO, the scorpion")
    elif(dd>22 and dd<=30):
        print("You are SAGITTARIUS, the archer")
    else:
        print("Invalid Input")

elif(mm==12):
    if(dd<=23):
        print("You are SAGITTARIUS, the archer")
    elif(dd>23 and dd<=31):
        print("You are CAPRICORN, the goat")
    else:
        print("Invalid Input")