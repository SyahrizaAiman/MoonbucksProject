import random
 
#allocate page in the frame
def pageAllocation(filename, num_of_pages ,num_of_frames):
    file = open(filename, 'w')
    frames = [0] * num_of_frames
    pages = [0] * num_of_pages
    for x in range(0, len(frames)):
        frames[x] = None
    for x in range(0, len(pages)):
        while True:
            frame_num = random.randint(0, len(frames)-1) #randomize the allocation of page in the frame
            if (frames[frame_num] == None): #if frame is empty then put None
                break
            else:
                continue
        #info about where page is allocated
        print("Page " + str(x) + " is placed in Frame " + str(frame_num))
        frames[frame_num] = x
        pages[x] = frame_num
    for x in range(0, len(frames)):
        file.write(str(frames[x]) + ",")
    file.write('\n')
    for x in range(0, len(pages)):
        file.write(str(pages[x]) + ",")
    file.close()
 
#display tables containing frame address and page number
def displayTables(filename):
    file = open(filename, "r")
    frames = file.readline().split(",")
    pages = file.readline().split(",")
    frames.remove('\n')
    pages.remove('')
    print("\n--------------Page Map Table----------------")
    print("Page Number           |  Page Frame")
    for x in range(0, len(pages)):
        print(str(x) + "                     |  " +str(pages[x]))
    print("-------------------------------------------\n")
    print("------------Memory Map Tables---------------")
    print("Frame Address      |   Page Number")
    for x in range(0, len(frames)):
        if (frames[x] == None):
            print(str(x) + "                  |     " +  "Empty")
        else:
            print(str(x) + "                  |     " +str(frames[x]))
    print("-----------------------------------------\n")
    file.close()
 
#get the physical address
def getPhysicalAddress(filename, frame_Size):
    file = open(filename, "r")
    frames = file.readline().split(",")
    pages = file.readline().split(",")
    frames.remove('\n')
    pages.remove('')
    pages = [int(x) for x in pages]
    base_address = int(input("Enter the base address: "))
    logical_address = int(input("Enter the logical address:  "))
 
    page_address = int(logical_address / frame_Size)
    offset = int(logical_address % frame_Size)
    print("Page address: " + str(page_address))
    print("Offset: " + str(offset))
    physical_address = base_address + (pages[page_address]*frame_Size) + offset
    print("The physical address is: " + str(physical_address))
    file.close()
 
if __name__ == '__main__':
        physical_memory = int(128)
        logical_memory = int(64)
        frame_size = int(16)
 
 
        print("The physical memory size: " + str(physical_memory))
        print("The logical memory size: " + str(logical_memory))
        print("The partition size: " + str(frame_size))
 
        num_of_frames = int(physical_memory/frame_size)
        num_of_pages = int(logical_memory/frame_size)
 
        print("The number of pages in the logical memory: " +str(num_of_pages))
        print("The number of frames available in physical memory: " + str(num_of_frames))
        # filename = open('lab6.text', 'w')
        # filename.close()
        filename = "lab6.txt"
        # with open('C:\Users\ASUS\Desktop\sem 4\WIA2004 OS\Lab\lab6.txt') as f:
 
        pageAllocation(filename, num_of_pages, num_of_frames)
        displayTables(filename)
        getPhysicalAddress(filename, frame_size)
