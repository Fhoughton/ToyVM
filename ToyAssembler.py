import sys

fname = sys.argv[1]
outbytes = ""

#Process arguments
def decode_value(value,cnt):
    out = ""
    if value[0] == "R":
        out+="0"
    elif value[0] == "#":
        out+="1"
    elif value[0] == ";":
        return -1
    else:
        print("Error: Failed to decode value at line {}".format(cnt))
        
    value = value[1:]
    
    binval = "{0:b}".format(int(value))
    
    if len(binval) > 8:
        print("Error: Value greater than 8 bits, can't convert at line {}".format(cnt))
    else:
        while len(binval) < 8:
            binval = "0"+binval #Pad with zeroes till it's 8 bits
    
    out+=binval
    
    return out

with open(fname) as fp:
    line = fp.readline()
    cnt = 0
    while line:
        cnt+=1
        expr = line.split(" ")
        if expr[0] == "STR":
            outbytes+="00" #STR, stores a value into a register, instruction 0
        elif expr[0] == "ADD":
            outbytes+="01" #ADD, adds a value to another value and stores the result in a selected register, instruction 1
        elif expr[0] == "MUL":
            outbytes+="10" #MUL, multiplies a value by another value and stores the result in a selected register, instruction 2
        elif expr[0] == "OUT":
            outbytes+="11" #OUT, prints the value from a register out to the console, instruction 3
        else:
            print("Error: Unknown instruction at line {}".format(cnt))
            
        for i in range(len(expr)):
            k = decode_value(expr[i+1],cnt)
            if k != -1:
                outbytes+=k
            else:
                break
        line = fp.readline()
    
print("Assembled into "+fname.split(".")[0]+".s")

f = open(fname.split(".")[0]+".s", "w")
f.write(outbytes)
f.close()