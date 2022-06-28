from math import trunc
ans = []
def remComma(num):
    #deck1 = []
    deck = ""
    nums = str(num)
    deck1 = nums.split(",")
    #for i in nums:
       # if i != ",":
            #continue
          #  deck1 .append(i)

    for i in deck1:
        deck +=i
    return(int(deck))

def wordify(num):
    if num == 1:
        return "ONE "
    if num == 2:
        return "TWO "
    if num == 3:
        return "THREE "
    if num == 4:
        return "FOUR "
    if num == 5:
        return "FIVE "
    if num == 6:
        return "SIX "
    if num == 7:
        return "SEVEN "
    if num == 8:
        return "EIGHT "
    if num == 9:
        return "NINE "
    if num == 0:
        return "ZERO "
     
def wordifytens(num):
    if num == 1:
        return "TEN "
    if num == 2:
        return "TWENTY "
    if num == 3:
        return "THIRTY "
    if num == 4:
        return "FORTY "
    if num == 5:
        return "FIFTY "
    if num == 6:
        return "SIXTY "
    if num == 7:
        return "SEVENTY "
    if num == 8:
        return "EIGHTY "
    if num == 9:
        return "NINTY "

def wordifyteenage(num):
    if num == 1:
        return "ELEVEN "
    if num == 2:
        return "TWELVE "
    if num == 3:
        return "THIRTEEN "
    if num == 4:
        return "FOURTEEN "
    if num == 5:
        return "FIFTEEN "
    if num == 6:
        return "SIXTEEN "
    if num == 7:
        return "SEVENTEEN "
    if num == 8:
        return "EIGHTEEN "
    if num == 9:
        return "NINTEEN "
    if num == 0:
        return "TEN "

def truncer(num):
    x = len(str(num))
    power = 10 **(x-1)
    mainnum = num//power
    trunced = num - (mainnum * power)
    return trunced

def index(num):
    x = len(str(num))
    power = 10 **(x-1)
    return num // power

def big(num, power, suffix):
    if num == 1:
        ans.append(wordify(power))
        ans.append(suffix)
    
    if num == 2:
        ans.append(wordifytens(power))
    
    if num == 3:
        ans.append(wordifyteenage(power))
        ans.append(suffix)
    
def tenChecker(tens,units,suffix):
    if tens == 1:
            big(3,units, suffix)

    if tens > 1 and units > 0:
            big(2,tens, suffix)

    if tens > 1 and units == 0:
            big(2,tens,suffix)
            ans.append(suffix)

def numberToWords(num):
    snum = str(num)
    if num >= 10000000000:
        return "Number is too big for this program"
    
    if num == 0:
        wordify(num)
    
    bill = index(num)
    cbill = truncer(num)
    if  len(snum)< 10:
        cbill = num
        bill = 0
        
    
    hunmil = index(cbill)
    chunmill = truncer(cbill)
    if  len(snum)< 9:
        chunmill = num
        hunmil = 0
    

    tenmil = index(chunmill)
    ctenmil = truncer(chunmill)
    if len(snum) < 8:
        ctenmil = num
        tenmil = 0
    
    mil = index(ctenmil)
    cmil = truncer(ctenmil)
    if  len(snum)< 7:
        cmil = num
        mil = 0
    
    hunthou = index(cmil)
    chunthow = truncer(cmil)
    if  len(snum)< 6:
        chunthow = cmil
        hunthou = 0

    tenthou = index(chunthow)
    ctenthow = truncer(chunthow)
    if  len(snum)< 5:
        ctenthow = num
        tenthou = 0

    thousand= index(ctenthow)
    cthou = truncer(ctenthow) #the number with it's thousandth digit taken off
    
    if  len(snum)< 4:
        cthou = num
        thou = 0
    else:
        thou = thousand
    
    hund = index(cthou)
    chun = truncer(cthou) #the number with it's hundreth digit taken off
    
    if  len(snum)< 3:
        chun = num
        hun = 0
    else:
        hun = hund
    
    tenth = index(chun)
    cten = truncer(chun)

    if  len(snum)< 2:
        cten = num
        ten = 0
    else:
        ten = tenth
        cten = cten
    
    unit = cten

    if bill > 0:
        big(1,bill,"BILLION ")

    if hunmil > 0:
        big(1,hunmil, "HUNDRED ") ##

    if (bill > 0 or hunmil > 0) and (tenmil > 0 or mil > 0):
        ans.append("AND ")
    
    if tenmil>0:
        tenChecker(tenmil, mil,"")

    if mil > 0 and tenmil != 1:
        big(1,mil,"")

    if hunmil or tenmil or mil > 0:
        ans.append("MILLION ")

    if hunthou > 0:
        big(1,hunthou, "HUNDRED ")    

    if ( hunthou > 0) and (tenthou or thou >0 or hun > 0):
        ans.append("AND ")

    if tenthou > 0:
        tenChecker(tenthou,thou,"")
    
    if thou>0 and tenthou != 1:
        big(1,thou,"")
    
    if hunthou or thou or tenthou > 0:
        ans.append("THOUSAND ")

    if hun > 0:
        big(1,hun,"HUNDRED ")
        
    if (bill or hunmil or tenmil or mil or hunthou or tenthou or thou >0 or hun > 0) and (ten > 0 or unit > 0):
        ans.append("AND ")
    
    if ten > 0:
        ans.append(tenChecker(ten,unit,""))
        
    
    if unit > 0 and ten != 1:
        ans.append(wordify(unit))
        

    result = "The answer is "
    for k in ans:
        if k != None:
            result += k 
    
    #print(ans) 
    # print("bil = ",bill,"cbil = ",cbill)
    # print("hml = ",hunmil,"chml = ",chunmill)
    # print("tml = ",tenmil,"ctml = ",ctenmil)
    # print("mil = ", mil,"cmil = ",cmil)
    # print("hth = ", hunthou, "chth = ",chunthow)
    # print("tth = ",tenthou, "ctth = ", ctenthow)
    # print("thu = ",thou,"cthu = ",cthou)
    # print("hun = ",hun,"chun = ",chun)
    # print("ten = ",ten,"cten = ",cten)
    # print("uni = ",unit)

    return result

#num = int(input("Enter Number= "))
num = 1000000000
#print(remComma(num))
print(numberToWords(num))
