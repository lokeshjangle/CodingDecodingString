# //Program to create coding and decoding string
import string
import random
print("Write exit if you want to exit")
while True:
    st = input("Enter the message:")
    if st == "exit":
        exit()
    else:
        words = st.split(" ")
        coding = int(input("1. Coding\n2. Decoding\n"))
        coding = True if (coding == 1) else False
        # print(coding)
        if(coding):
            nwords = []
            for word in words:
                if (len(word)>=3):
                    r1 = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase,k=3))
                    r2 = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=3))
                    stnew = r1 + word[1:] + word[0] + r2
                    nwords.append(stnew)
                else:
                    nwords.append(word[::-1]) #reverse string
            print(" ".join(nwords))
        else:
            nword = []
            for word in words:
                if (len(word)>=3):
                    stnew = word[3:-3]
                    stnew = stnew[-1] + stnew[:-1]
                    nword.append(stnew)
                else:
                    nword.append(word[::-1])
            print(" ".join(nword))