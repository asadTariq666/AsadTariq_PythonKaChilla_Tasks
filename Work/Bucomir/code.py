count = 0
Z = 0
X= 0
Y =0
flag = 0
# variables ( just make changes by keeping up the format)
var1 ="[0.000000,0.000000,1.000000,0.000000]"
var2 = "[0,0,0,0]"
var3 = "[9E9,9E9,9E9,9E9,9E9,9E9]]"
var4 = "printSpeed"
var5 = "z0"
var6 = "bendedTool"
var7 = "\WObj:=wobj0;"

f = open("input.txt", "r")
w = open("output.txt", "w")
Lines = f.readlines()
for line in Lines:
    
    if line.__contains__('LAYER:0'):
        flag =1
    if (flag):
        if line.__contains__('Z'):
          #print(line,count)
          splitted_line = line.split()
          Z = splitted_line[4].replace("Z", "")
          #print(Z)

        if((line.__contains__('G1 ') or line.__contains__('G0 ')) and line.__contains__('X') and line.__contains__('Y')):
            splitted_line = line.split()
            for i in range(len(splitted_line)):
                if(splitted_line[i].__contains__('G0')):
                    move = splitted_line[i].replace("G0", "MoveJ")
                if(splitted_line[i].__contains__('G1')):
                    move = splitted_line[i].replace("G1", "MoveL")
                if(splitted_line[i].__contains__('X')):
                    X = splitted_line[i].replace("X", "")
                if(splitted_line[i].__contains__('Y')):
                    Y = splitted_line[i].replace("Y", "")
            new_line = move+'[['+X+','+Y+','+Z+ "]," +var1+  ','  + var2  +','  + var3  +',' + var4  +',' + var5 +',' + var6 +',' + var7 + "\n"
            #str = ','.join(new_line)
            #print(type(new_line))
            #print(new_line)
            w.write(new_line)
                #count +=1
f.close()
w.close()

