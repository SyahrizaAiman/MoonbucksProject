import random

def findWaitingTime(proc,n, wt):
    wt[0] = 0
    for i in range(1, n ):
        wt[i] = proc[i - 1][1] + wt[i - 1]

# Function to calculate turn around time
def findTurnAroundTime(proc, n, wt, tat):
    #calc turnaround time by
    #adding proc[i][1](burst) + wt[i]
    for i in range(n):
        tat[i] = proc[i][1] + wt[i]

# Function to calculate waiting time
# and turn-around times.
def print_FCFS_SJF(proc, n):
    wt = [0] * n
    tat = [0] * n

    # Function to find waiting time before sorting
    # of all processes
    findWaitingTime(proc, n, wt)

    # Function to find turn around time before sorting
    # for all processes
    findTurnAroundTime(proc, n, wt, tat)

    print("\n------------------------------FCFS-------------------------------------- \n Processes   Burst Time    Waiting"
                    "Time      Turn-Around Time ")
    for i in range(n):
        print(" ", proc[i][0], "\t\t",
                proc[i][1], "\t\t",
                wt[i], "\t\t", tat[i] )
    
    #sort the process according to their burst time
    proc.sort(key= lambda x:x[1])

    # Function to find waiting time after sorting
    # of all processes 
    findWaitingTime(proc, n, wt)

    # Function to find turn around time before sorting
    # for all processes
    findTurnAroundTime(proc, n, wt, tat)
  
    # Display processes along with all details
    print("\n------------------------------SJF--------------------------------------\n Processes    Burst Time     Waiting",
                    "Time     Turn-Around Time")

    for i in range(n):
        print(" ", proc[i][0], "\t\t",
                proc[i][1], "\t\t",
                wt[i], "\t\t\t", tat[i])

      
#Process id's and burst time
print("*****Made by GROUP 4 Operating System Tutorial 5*****\n")

print("FCFS and SJF")

proc_index = (random.randint(1,10))
print("There are " + str(proc_index) + " process(s)")

proc=[]

for i in range(proc_index):
        proc.append([i+1,int(random.randint(1,10))])


n = len(proc)
print_FCFS_SJF(proc, n)
print("\nOrder in which process get executed:")
#sort using 2nd element
proc.sort(key= lambda x:x[1])
#print only first element of 2d array
print([i[0] for i in proc])