package LabOS;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
//First Fit Method
public class Lab5new{
    
    static void bestFit(int processSize[], int n, int blockSize[], int m)
    {
        // Array allocation stores block id of the block allocated to a process
        int allocation[] = new int[n];
        int originalBlockSize[] = blockSize.clone(); //for printing
        
        // At first, no block will be assigned to any process
        for (int i = 0; i < allocation.length; i++)
            allocation[i] = -1;

        int allocated[] = new int[m];
        for (int j = 0; j < m; j++)
            allocated[j] = -1;

        // for each number of process
        for (int i=0; i<n; i++)
        {
            int bestIndex = -1;
            // Find the block that fits the best for current process
            for (int j=0; j<m; j++)
            {
                if ((blockSize[j] >= processSize[i])&&allocated[j]==-1)
                {
                    if (bestIndex == -1)
                        bestIndex = j;
                     else if (blockSize[bestIndex] > blockSize[j])
                         bestIndex = j;
                }
            }

            // If we could find a block to allocate for current process
            if (bestIndex != -1)
            {
                // allocate block j to p[i] process
                allocation[i] = bestIndex;
                allocated[bestIndex] = i;

                // Reduce available memory in this block.
                blockSize[bestIndex] -= processSize[i];
            }
        }

        System.out.printf("%10s %13s %10s %21s %21s %n","Process No.","Process Size","Block No.","Original Block Size", "Available Block Size");
        for (int i = 0; i < n; i++)
        {
            System.out.printf("%5d %14d",(i+1),processSize[i]);
            if (allocation[i] != -1)
                System.out.printf("%12d %16d %20d", allocation[i] + 1, originalBlockSize[allocation[i]], blockSize[allocation[i]]);
            else
                System.out.printf("%12s","-" );
            System.out.println();
        }
    }
  
    static void firstFit(int processSize[], int n, int blockSize1[], int m)
    {
        // Array allocation stores block id of the block allocated to a process, -1 if no block fits the process size
        int allocation[] = new int[n];
        for (int i = 0; i < allocation.length; i++)
            allocation[i] = -1;
        
        // Array allocated stores the process id allocated to the block, -1 if no process being allocated to the block
        int allocated[] = new int[m];
        for (int j = 0; j < m; j++)
            allocated[j] = -1;

        int originalBlockSize[] = blockSize1.clone(); //for printing purposes

        // for each number of process
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                // find block that fits the current process size and hasn't being allocated
                if ((blockSize1[j] >= processSize[i]) && allocated[j]==-1)
                {
                    // allocate block j to p[i] process
                    allocation[i] = j;
                    allocated[j] = i;

                    // Reduce available memory in this block.
                    blockSize1[j] -= processSize[i];
                    break;
                }
            }
        }

        // printing the output
        System.out.printf("%10s %13s %10s %21s %21s %n","Process No.","Process Size","Block No.","Original Block Size", "Available Block Size");
        for (int i = 0; i < n; i++)
        {
            System.out.printf("%5d %14d",(i+1),processSize[i]);
            if (allocation[i] != -1)
                System.out.printf("%12d %16d %20d", allocation[i] + 1, originalBlockSize[allocation[i]], blockSize1[allocation[i]]);
            else
                System.out.printf("%12s","-" );
            System.out.println();
        }
    }

    //convert Integer[] to int[]
    public static int[] toPrimitive(Integer[] Integer) {

		int[] blockSize = new int[Integer.length];
		for (int i = 0; i < Integer.length; i++) {
			blockSize[i] = Integer[i].intValue();
		}
		return blockSize;
    }

    // Main method
    public static void main(String[] args)
    throws IOException
    {
    
        // list that holds int of a file
        List<Integer> listOfInt = new ArrayList<Integer>();
           
        // load data from file
        BufferedReader bf = new BufferedReader(
        new FileReader("LabOS\\Lab5.txt"));
               
        // read entire line as int
        int line = Integer.parseInt(bf.readLine());
               
        // checking for end of file
         while (line != 0) {
            listOfInt.add(line);
            line = Integer.parseInt(bf.readLine());
            }
               
        // closing bufferreader object
        bf.close();
               
        // storing the data in arraylist to array
        Integer[] BS = listOfInt.toArray(new Integer[0]);
        int blockSize[] = toPrimitive(BS);
        int blockSize1[] = toPrimitive(BS);
        // generate random process size
        Random R = new Random();
        int n = R.nextInt(5-2+1)+2;
        int processSize[] = new int [n];
        for(int i=0;i<n;i++){
            processSize[i] = R.nextInt(500+1);
        }
        int m = blockSize.length;
        //int n = processSize.length;

            
        //invoke Best Fit method
        System.out.println("\nBest Fit");
        bestFit(processSize, n, blockSize, m);
        
        
        // invoke First Fit method
        System.out.println("\nFirst Fit");
        firstFit(processSize, n, blockSize1, m);

    }
}
