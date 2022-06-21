import random

def SeqFile(start, length):
    count  = 0

    for i in range(start, start+length):
        if Block[i] == 0:
             count +=1

    if length == count:
        for i in range (start, start + length):
            if Block[1] == 0:
               Block[i] = 1
            print (f"{i}")
        print("The file is allocated\n")
    else:
        print("The file is not allocated\n")
    print("----------------------------------------")

if __name__ =="__main__":
    f = open("LabOS\Lab3.txt", "r")
    File = int(f.read())
    Block = [0] * 60
    print("\n--------/Sequential File Allocation\--------")
    print("Files allocated at:\n")

    for i in range (File):
        start = random.randint(0,60)
        length = random.randint(1,10)

        while start + length > 60:
            start = random.randint(0, 60)
            length = random.randint(1,10)

        print(f"Starting block: {start}")
        print(f"Length of file: {length}")
        SeqFile(start, length)
