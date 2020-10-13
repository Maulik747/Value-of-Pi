import math
import random
needle_results=[]
angle_results=[]
for i in range(1000):
    needle_results.append(random.uniform(0,1))
    angle_results.append(random.uniform(0,math.pi))

counter=0
for a in needle_results: #independent random variables a and b
    for b in angle_results:
        if(a<=0.5* math.sin(b) or (1-a)<=0.5*math.sin(b)): #probability distribution limits.
            counter=counter+1


p=(float)(counter/1000000)
answer=2/p #close approximation of the value of PI.
print(answer)

