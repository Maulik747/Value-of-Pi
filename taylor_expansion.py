import math
x=float(0.5) #computing taylor series at 0.5
denom=2
numer=1
final_value=0
for i in range(1,10):
    numer=numer*(numer+2)#numerator of taylor expansion
    denom=denom*(denom+2)#denominator of taylor expansion
    e=2*i+3
    final_value=final_value+((numer/denom)*(pow(x,e)/e))#summing the terms

print(("The approximated value of pi is:",final_value+x+(0.5*(pow(x,3)/3)))*6) #adding some missing terms.


 