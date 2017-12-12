#!/usr/bin/env python

import math
import matplotlib.pyplot as plt

def f(x):
    answer = math.pow(math.sin(x-2),2) * math.pow(math.e,- (math.pow(x,2)));
    return answer;


input = [];
output = [];


iter = 0;

while iter <= 2:
    input.append(iter);
    iter+= 0.08;

iter = 0;


while iter < len(input):
    output.append(f(input[iter]));
    iter += 1;

print (output);
print(math.pi);
plt.xlabel("X-Axis");
plt.ylabel("Y-Axis");
plt.title("sin^2(x-2)e^(-x^2)");
plt.ylim(0,1.5);
plt.xlim(0,2.5);
plt.plot(input,output);
plt.show()



