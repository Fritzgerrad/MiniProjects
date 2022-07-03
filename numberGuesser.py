import random
num = int(random.randrange(-1,11))
count = 0

def guess(): 
    global num
    global count
    yournum = int(input("Guess the number "))
    if yournum == num:
        print("Yes my number is ",num," You guessed it right and it only took you ",count," tries.") 
        quit()

    else:
        if count >3 and count<5:
            print("Wrong guess ,try again")
            print("Here's a hint: it's less than ",num+5," and greater than ",num-5)
            print(count)
            count +=1
            guess()

        if count >5:
            print("Wrong guess, try again")
            print("Here's a hint: it's less than ",num+3," and greater than ",num-3 )
            count +=1
            print(count)
            guess()
        
        else:
            print("Wrong guess, try again")
            count +=1
            guess()

guess()