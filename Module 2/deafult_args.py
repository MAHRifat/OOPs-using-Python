def sum(n1,n2,n3=0,n4=0,n5=0,n6=0,n7=0):
    re=n1+n2+n3+n4+n5+n6
    return re
total = sum(34,34,6,4)
print(total)

# args
def all_sum(num1,num2,*n):
    s=num1+num2
    for num in n:
       s+=num
    return s

tot=all_sum(34,35,343,3,4,43,34,34.54,.23,4)
print(tot)