S = input()
l=[]
count = 0
c_L=0
c_R=0
S_update = ''

for char in S:
    if 'L' in char:
        c_L=c_L+1
        S_update=S_update+char
        if c_R == c_L:
            count = count+1
            c_L=0
            c_R=0
            l.append(S_update)
            S_update=''
    elif 'R' in char:
        c_R=c_R+1
        S_update=S_update+char
        if c_R == c_L:
            count = count+1
            c_L=0
            c_R=0
            l.append(S_update)
            S_update=''

print(count)
for s in l:
    print(s)