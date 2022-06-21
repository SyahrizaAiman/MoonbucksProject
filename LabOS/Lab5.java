package LabOS;
import java.util.Random;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
//First Fit Method
public class Lab5{

    static void firstFit(int processSize[], int n, int blockSize[], int m)
    {
        // Array allocation stores block id of the block allocated to a process, -1 if no block fits the process size
        int allocation[] = new int[n];
        for (int i = 0; i < allocation.length; i++)
            allocation[i] = -1;
        
        // Array allocated stores the process id allocated to the block, -1 if no process being allocated to the block
        int allocated[] = new int[m];
        for (int j = 0; j < m; j++)
            allocated[j] = -1;

        int originalBlockSize[] = blockSize.clone(); //for printing purposes

        // for each number of process
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < m; j++)
            {
                // find block that fits the current process size and hasn't being allocated
                if ((blockSize[j] >= processSize[i]) && allocated[j]==-1)
                {
                    // allocate block j to p[i] process
                    allocation[i] = j;
                    allocated[j] = i;

                    // Reduce available memory in this block.
                    blockSize[j] -= processSize[i];
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
                System.out.printf("%12d %16d %20d", allocation[i] + 1, originalBlockSize[allocation[i]], blockSize[allocation[i]]);
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

        //int processSize[] = {0, 0, 0, 0};
        Random R = new Random();
        int n = R.nextInt(5-2+1)+2;
        int processSize[] = new int [n];
        for(int i=0;i<n;i++){
            processSize[i] = R.nextInt(600+1);
        }
        int m = blockSize.length;
        //int n = processSize.length;

        System.out.print("--------------------------------------------------------------------------\n");
        System.out.print("----------------------------------First Fit-------------------------------\n");
        System.out.print("--------------------------------------------------------------------------\n");


        // invoke First Fit method
        firstFit(processSize, n, blockSize, m);

    }
}