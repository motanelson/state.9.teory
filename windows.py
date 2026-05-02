#change next 2 lines
winas="c:\\MinGW\\bin\\as.exe"
winobj="c:\\MinGW\\bin\\objdump.exe"
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
os.system(winobj+" -x "+a+" > out.txt")

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
            if len(aa)>8:
                 print(aa[9])
        if a.strip()=="SYMBOL TABLE:":
             t=True
print("give me the .o symbol name to display? ")
b=input().strip()
t=False
for a in txts:
    aa=spt(a)
    if len(aa)>0:
        if t:
            if len(aa)>8:
                if aa[9].strip()==b:
                    print(aa[9]+" = "+aa[8])
        if a.strip()=="SYMBOL TABLE:":
             t=True
