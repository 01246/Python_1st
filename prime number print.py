number=int(input("give input"))
divisor=2
prime=True
while (number>divisor) :
    if number%divisor==0:
        prime=False
        print("not prime")
        break
    else:
        divisor=divisor+1
    print("prime")
