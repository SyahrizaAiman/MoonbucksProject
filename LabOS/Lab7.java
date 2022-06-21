package LabOS;
import java.io.*;
import java.util.*;

public class Lab7 {
    static String pathname = "Lab7.txt";
    static File file = new File(pathname);
    static Scanner scanner;
    static int n, m;
    static int safe[] = new int[n + 10];
    static int resource_available[], resource_allocation[][], resource_need[][], change_required[][], maximum_allocations[][];
 
    static void declare_scanner() throws FileNotFoundException {
        scanner = new Scanner(file);
    }
 
    static void read_maximum_allocation() {
        maximum_allocations = new int[n][m];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                maximum_allocations[i][j] = scanner.nextInt();
    }
 
    static void read_resource_allocation() {
        resource_allocation = new int[n][m];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                resource_allocation[i][j] = scanner.nextInt();
    }
 
    static void read_resource_available() {
        resource_available = new int[m];
        for (int i = 0; i < m; i++)
            resource_available[i] = scanner.nextInt();
    }
 
    static void read_resource_need() {
        resource_need = new int[n][m];
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                resource_need[i][j] = maximum_allocations[i][j] - resource_allocation[i][j];
    }
 
    static void setChange_required() {
        change_required = new int[n][m];
 
        System.out.println("Max matrix is: ");
        for(int a = 0; a<m;  ){
            System.out.print("\t\t");
            for (char ch = 'A' ; a<m ; ch++){
                System.out.print(ch + " ");
                a++;
            }
           
        }
        System.out.println();
        for (int i = 0; i < n; i++) {
            System.out.print("Process " + (i+1) + "\t");
 
            for (int j = 0; j < m; j++) {
                System.out.print(maximum_allocations[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
 
        System.out.println("Allocation matrix is: ");
        for(int a = 0; a<m;  ){
            System.out.print("\t\t");
            for (char ch = 'A' ; a<m ; ch++){
                System.out.print(ch + " ");
                a++;
            }
           
        }
        System.out.println();
 
        for (int i = 0; i < n; i++) {
            System.out.print("Process " + (i+1) + "\t");
            for (int j = 0; j < m; j++) {
                System.out.print(resource_allocation[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
 
        System.out.println("Need matrix is: ");
 
        for(int a = 0; a<m;  ){
            System.out.print("\t\t");
            for (char ch = 'A' ; a<m ; ch++){
                System.out.print(ch + " ");
                a++;
            }
           
        }
        System.out.println();
     
        for (int i = 0; i < n; i++) {
            System.out.print("Process " + (i+1) + "\t");
            for (int j = 0; j < m; j++) {
                System.out.print(resource_need[i][j] + " ");
            }
            System.out.println();
        }
    }
 
    static void print_all() {
        System.out.println();
        System.out.println("Safe sequence is :");
        for (int i = 0; i < n; i++) {
            System.out.print("Process ");
            System.out.print((char) ( + '1' + safe[i]) + " ==> ");
        }
        System.out.println("done");
        System.out.println("\n");

        System.out.println("Change in available resource matrix : ");
        for (int i = 0; i < n; i++) {
            System.out.print("Snapshot " + (i+1) + "");
            for(int a = 0; a<m;  ){
                System.out.print("\t\t");
                for (char ch = 'A' ; a<m ; ch++){
                    System.out.printf("%-4s",ch);
                    a++;
                }
                System.out.println();
                System.out.print("\t\t\t");
            }
            for (int j = 0; j < m; j++) {
                System.out.printf("%-2d  ", change_required[i][j]);
            }
            System.out.println();
            System.out.println();
        }
    }
 
    public static boolean bankersAlgo() {
        //n = number of process
        //m = number of resource type
        boolean safe_check[] = new boolean[n];
        for (int i = 0; i < n; i++)
            safe_check[i] = false;
        int count_check = 0;
        int loop_count = 0;
        do {
            for (int i = 0; i < n; i++) {
                boolean flag = true;
                if (safe_check[i] == false) {
                    for (int j = 0; j < m; j++) {
                        if (resource_available[j] < resource_need[i][j])
                            flag = false;
                    }
                    if (flag == true) {
                        for (int j = 0; j < m; j++) {
                            resource_available[j] = resource_available[j] + resource_allocation[i][j];
                            change_required[count_check][j] = resource_available[j];
                        }
                        safe[count_check] = i;
                        safe_check[i] = true;
                        count_check++;
                    }
                }
 
            }
            loop_count++;
        } while (loop_count < n && count_check < n);
 
        return !(count_check > n);
    }
 
    public static void main(String[] args) throws FileNotFoundException {
        declare_scanner();
        n = scanner.nextInt();
        m = scanner.nextInt();
        System.out.println("\n--------------DECLARING THE NUMBER OF PROCESSES AND RESOURCES---------------");
        System.out.println("The number of process(es) is " + n);
        System.out.println("The number of resource(s) type is " + m + "\n");
        read_maximum_allocation();
        read_resource_allocation();
        read_resource_available();
        read_resource_need();
        setChange_required();
        boolean system_is_safe = bankersAlgo();
        if (system_is_safe) {
            print_all();
        } else{
            System.out.println("System is in unsafe state");
        }
    }

}
