# Write your code here
# Number of barriers
n = int(input())

#hold the barriers coordinates
barriers = []

# get the coordinates from the user
for i in range(n):
    [x,y,d] = [int(c) for c in input().split()] 
    barriers.append([x,x+d])

#sorting the barriers
barriers.sort()

#initialize the counter
blocked_ants = 0
marker = 0


# block ants in the coordinates
for barrier in barriers:
    if(barrier[0] >= marker):
        marker = barrier[0]
        if(marker < barrier[1]):
            blocked_ants = blocked_ants + (barrier[1] - marker)+1
            marker = barrier[1]+1
    elif(marker <= barrier[1]):
            blocked_ants = blocked_ants + (barrier[1] - marker)+1
            marker = barrier[1]+1

#printing the total number of blocked ants
print (blocked_ants)
