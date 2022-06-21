#include<stdio.h>
#include<conio.h>
#define max 25

void main()
{
    int i,j,numBlock,numFile,temp,fragment[max],b[max],f[max],lowest=10000;
    static int bf[max],ff[max];

    printf("\n~~~~~~~~~~Best Fit~~~~~~~~~~\n");
    printf("\nInsert the number of blocks:");
    scanf("%d",&numBlock);
    printf("Insert the number of files:");
    scanf("%d",&numFile);
    printf("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
    printf("\nInsert the size of the blocks:\n");
    for(i=1;i<=numBlock;i++){
        printf("Block %d:",i);scanf("%d",&b[i]);
    }
    printf("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n");
    printf("\nInsert the size of the files :\n");

    for(i=1;i<=numFile;i++)
    {
        printf("File %d:",i);
        scanf("%d",&f[i]);
    }

    for(i=1;i<=numFile;i++)
    {
        for(j=1;j<=numBlock;j++)
        {
            if(bf[j]!=1)
            {
                temp=b[j]-f[i];
                if(temp>=0)
                    if(lowest>temp)
                    {
                        ff[i]=j;    
                        lowest=temp;
                    }
            }
        }
        fragment[i]=lowest;
        bf[ff[i]]=1;
        lowest=10000;
    }
    printf("\n---------------------------------------------------------------------------");
    printf("\nFile No\t\tFile Size \tBlock Number\tBlock Size\tFragment");
    printf("\n---------------------------------------------------------------------------");
    for(i=1;i<=numFile && ff[i]!=0;i++)
    printf("\n%d\t\t%d\t\t%d\t\t%d\t\t%d",i,f[i],ff[i],b[ff[i]],fragment[i]);
    printf("\n---------------------------------------------------------------------------\n");
}