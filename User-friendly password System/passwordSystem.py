import string
def hashfunct(str1):
    print ("Hash str: ",str1)
    p = 131
    M = (10**9)+7
    val=0
    l= len(str1)
    print(l)
    for i,char in enumerate(str1):
        # print('i',i)
        val = val + (ord(char)* ((p)**(l-(i+1))))
    return val % M
    
def authEvents(events):
    appendcharstr= string.ascii_lowercase + string.ascii_uppercase + string.digits
    print(appendcharstr)
    result=[]
    
    cpasshv = 0
    appendhashset=None
    for event in events:
        if(event[0]=="setPassword"):
            
            cpasshv = hashfunct(event[1])
            appendhashset = set(hashfunct(event[1]+x) for x in appendcharstr)
            print(appendhashset)
            print("actual password hash: ",cpasshv)
        elif(event[0]=="authorize"):
            print("Authorized password hash: ",event[1])
            print("in set or not: ", int(event[1]) in appendhashset)
            if (int(event[1]) == cpasshv or int(event[1]) in appendhashset):
                result.append(1) 
            else:
                result.append(0)    
            print(result)    
    return result    

def main():
    value = [["setPassword", "000A"],
                 ["authorize", "108738450"],
                 ["authorize","108738449"],
                 ["authorize", "244736787"]]
    print(authEvents(value))

main()