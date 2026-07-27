import pandas as pd 
import numpy as np 

df= pd.read_csv("./StudentsPerformance.csv")


# mean 
scores = list(df["math score"])
total = 0
for num in scores:
    total += num

mean = total / len(scores)
print("Mean =", mean)

#median 
scores = sorted(list(df["math score"]))
n = len(scores)
if n % 2 == 1:
    median = scores[n // 2]
else:
    median = (scores[n // 2 - 1] + scores[n // 2]) / 2

print("Median =", median)

#Mode 

scores = list(df["math score"])
frequency = {}
for num in scores:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

max_count = 0
mode = None

for key in frequency:
    if frequency[key] > max_count:
        max_count = frequency[key]
        mode = key

print("Mode =", mode)
print("Frequency =", max_count)