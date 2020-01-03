import sys

fname = sys.argv[1]

#Registers
r0 = 0
r1 = 0
r2 = 0

def resolvearg(binfp):
    currarg =  binfp[:9]
    isregister = False
    
    if currarg[0] == "0": #Argument0 is a register
            isregister = True
    elif currarg[0] == "1": #Argument0 is a direct value
            isregister = False
    currarg = currarg[1:]
    
    currarg = int(currarg, 2)
    currarg = str(currarg)
    
    if isregister:
        currarg = "r" + currarg
    
    return (isregister,currarg)

with open(fname) as fp:
    binfp = fp.readline()
    instrlength = 0
    while binfp:
        currinstr = binfp[0]+binfp[1] #Read leftmost bit
        binfp = binfp[2:] #Remove opcode from stream
        
        if currinstr == "00": #STR, stores a value into a register
            arg0 = resolvearg(binfp)
            binfp = binfp[9:]
            arg1 = resolvearg(binfp)
            binfp = binfp[9:]
            
            if arg0[0] == True: #First argument must be register
                exec(arg0[1]+"="+arg1[1])

        elif currinstr == "01": #ADD, adds a value to another value and stores the result in a selected register
            arg0 = resolvearg(binfp)
            binfp = binfp[9:]
            arg1 = resolvearg(binfp)
            binfp = binfp[9:]
            arg2 = resolvearg(binfp)
            binfp = binfp[9:]
            
            if arg0[0] == True: #First argument must be register
                exec(arg0[1]+"="+arg1[1]+"+"+arg2[1])
        
        elif currinstr == "10": #MUL, multiplies a value by another value and stores the result in a selected register
            arg0 = resolvearg(binfp)
            binfp = binfp[9:]
            arg1 = resolvearg(binfp)
            binfp = binfp[9:]
            arg2 = resolvearg(binfp)
            binfp = binfp[9:]
            
            if arg0[0] == True: #First argument must be register
                exec(arg0[1]+"="+arg1[1]+"*"+arg2[1])
        
        elif currinstr == "11": #OUT, prints the value from a register out to the console
            arg0 = resolvearg(binfp)
            binfp = binfp[9:]
            
            if arg0[0] == True: #First argument must be register
                k = arg0[1]
                print(eval(k))