#DMAP Final Project Data 
#Simulating data 

#we will need the number of people coming to the line every 5 minutes, 
#then we also need to know how long people are in each bar so we know the flow of the line 




import random
import statistics

def generate_set():
    while True:

        nums = [random.randint(0, 50) for _ in range(3)]
        variance = statistics.variance(nums)
        

        if 0.5 <= variance <= 3:
            return nums
        
        
def generate_sets(n):
    sets = []
    for _ in range(n):
        sets.append(generate_set())
    return sets


n = 5
result = generate_sets(n)
for i, s in enumerate(result, 1):
    print(f"Set {i}: {s}, Variance: {statistics.variance(s):.2f}")
    
    
    
#Need to get the code to write to a file, not sure where it went? 