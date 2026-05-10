def limits(number,down,up):
    return min(up,max(number,down))


b=0
for a in range(-8,18):
    b=limits(a,0,10)
    print(b)