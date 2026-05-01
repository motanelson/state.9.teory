import os
def spt(s):
    r=s.split(" ")
    rr=[]
    for a in range(len(r)):
        
        if r[a].strip()!= "":
            rr.append(r[a])
    return rr
print("give me the .o object file name ? ")
a=input().strip()
os.system("objdump -x "+a+" > out.txt")

f1=open("out.txt","r")
txt=f1.read()
f1.close()
txts=txt.split("\n")
t=False
print("\033c")

for a in txts:
    aa=spt(a)
    if len(aa)>0:
        if t:
            if len(aa)<4:
                break
            print(aa[3])
        if a.strip()=="SYMBOL TABLE:":
             t=True
print("give me the .o symbol name to display? ")
b=input().strip()
t=False
for a in txts:
    aa=spt(a)
    if len(aa)>0:
        if t:
            if len(aa)<4:
                break
            #print(aa[3].strip())
            if aa[3].strip()==b:
                print(aa)
        if a.strip()=="SYMBOL TABLE:":
             t=True
