def IntToRoman(s):
    count = 0;
    m= (s // 1000)
    mc = s- (m*1000) 
    
    c = (mc// 100)
    cx = mc - (c*100)
    
    x = (cx // 10)
    
    a = cx - (x*10)
    
    strans =""
    ans = []
    if m>0 :
        for i in range(m):
            ans.append("M")
    
    if c>0:
        if c < 4:
            for i in range(c):
                ans.append("C")
        if c == 4:
            ans.append("CD")
        if c >= 5 and c<9:
            ans.append("D")
            for i in range (c-5):
                ans.append("C")
        if c == 9:
            ans.append("CM")
    if x>0:
            if x < 4:
                for i in range(x):
                    ans.append("X")
            if x == 4:
                ans.append("XL")
            if x >= 5 and x<9:
                ans.append("L")
                for i in range (x-5):
                    ans.append("X")
            if x == 9:
                ans.append("XC")
    if a>0:
            if a < 4:
                for i in range(a):
                    ans.append("I")
            if a == 4:
                ans.append("IV")
            if a >= 5 and a<9:
                ans.append("V")
                for i in range (a-5):
                    ans.append("I")
            if a == 9:
                ans.append("IX")
    for k in ans:
        strans += k
    print(strans)

IntToRoman(175) #CLXXV
IntToRoman(5658) #V
IntToRoman(4135) #MMMMCXXXIV
IntToRoman(999) #CDLVII
            