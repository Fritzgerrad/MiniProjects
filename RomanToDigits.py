def romanToInt(s):
        # """
        # :type s: str
        # :rtype: int
        # """
        #self.s = s
        count = 0
        prev = 0;
        for i in s:

            if i == 'I':
                count += 1
            
            if i == 'V' and prev == 'I':
                count += 3

            if i == 'V' and prev!= 'I':
                count += 5
                
            if i == 'X' and prev == 'I':
                count += 8
           
            if i == 'X' and prev != 'I':
                count += 10

            if i == 'L' and prev == 'X':                
                count += 30

            if i == 'L' and prev != 'X':
                count += 50

            if i == 'C' and prev != 'X':
                count += 100
            
            if i == 'C'and prev == 'X':
                count += 80
            
            if i == 'D'and prev == 'C':
                count += 300
            
            if i == 'D'and prev != 'C':
                count += 500
            
            if i == 'M'and prev == 'C':
                count += 800
            
            if i == 'M' and prev != 'C':
                count += 1000
            prev = i;    
            #print(prev)

        print(count)  

romanToInt("CMXI") #911
romanToInt("MCXI") #1111
romanToInt("MCIX") #1109
romanToInt("VII") #909



                