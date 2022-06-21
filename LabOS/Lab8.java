package LabOS;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Lab8 {
    public static void main(String args[]) throws FileNotFoundException
    {
        String pathname = "LabOS\\Lab8.txt";
        File file = new File(pathname);
        Scanner scanner = new Scanner(file);
        
        int pageFaults = 0;
        int incomingStream[];
        int frameSize;
        int incoming_stream_size;
        int m, n, s;

        frameSize = scanner.nextInt();
        incoming_stream_size = scanner.nextInt();
        incomingStream = new int[incoming_stream_size];
        for (int i=0; i<incoming_stream_size ; i++){
            incomingStream[i] = scanner.nextInt();
        }

        System.out.println("Incoming \t    Frame 1 \t     Frame 2 \t    Frame 3");
        int temp[] = new int[frameSize];
        for(m = 0; m < frameSize; m++)
        {
            temp[m] = -1; //initialize the frame with -1
        }

        for(m = 0; m < incoming_stream_size; m++)
        {
            s = 0;

            for(n = 0; n < frameSize; n++) //indicating the frame count
            {
                if(incomingStream[m] == temp[n])
                {
                    s++;
                    pageFaults--;
                }
            }
            pageFaults++;

            if((pageFaults <= frameSize) && (s == 0))
            {
                temp[m] = incomingStream[m];
            }
            else if(s == 0)
            {
                temp[(pageFaults - 1) % frameSize] = incomingStream[m];
            }

            System.out.println();
            System.out.print(incomingStream[m] + "\t\t\t");
            for(n = 0; n < frameSize; n++)
            {
                if(temp[n] != -1)
                    System.out.print(temp[n] + "\t\t");
                else
                    System.out.print("- \t\t");
            }
        }

        System.out.println("\n\nTotal Page Faults: " + pageFaults);
        int hit = incoming_stream_size - pageFaults;
        System.out.println("Page fault Ratio: " + (double) pageFaults/incoming_stream_size);
        System.out.println("Hits: " + hit);
        System.out.println("Hit Ratio : " + (double) hit/incoming_stream_size);
        System.out.println();
    }
}