def match_dream_eraser(string):
    index = 0
    length = len(string)
    while(index < length):
        sub_s = string[index:index+10]
        if(sub_s in ["", "dream", "dreamer", "erase", "eraser"]):
            return True

        sub_string1 = string[index:index+5]
        sub_string2 = string[index+5:index+10]
        if(sub_string1 == "dream"):
            if(sub_string2 == "erdre" or sub_string2 == "erera"):
                index += 7
            else:
                index += 5
        elif(sub_string1 == "erase"):
            if(sub_string2 == "rdrea" or sub_string2 == "reras"):
                index += 6
            else:
                index += 5
        else:
            return False

s = input()
kekka = match_dream_eraser(s)

if(kekka):
    print("YES")
else:
    print("NO")



