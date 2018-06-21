
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void Printpath(int x,int y,int result[x][y],char *X,char *Y);  
int max(int a, int b)
{
	return a > b? a: b;
}

void LongestCommonSubSequence(char *str1, char *str2, int len1, int len2)
{
	int lcs[len1+1][len2+1], i, j;
    for (i = 0; i <= len1; i++)
    {
    	for (j = 0; j <= len2; j++)
    	{
    		if (i == 0 || j == 0)
    			lcs[i][j] = 0;
    		else if(str1[i-1] == str2[j-1])
    			lcs[i][j] = lcs[i-1][j-1] + 1;
    		else
    			lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1]);
    	}
    }
    
     for (i = 0; i <= len1; i++)
    {
    	for (j = 0; j <= len2; j++)
    	{
                printf(" %d ", lcs[i][j]);
    	}
    	printf("\n");
    }
    Printpath(len1,len2,lcs,str1,str2);
}
void Printpath(int x,int y,int result[x+1][y+1],char *X,char *Y)
{
    int index=result[x][y]+1;
    char path[index];
    path[index]='\0';
    index--;
    int i,j;
    
    while((result[x][y]!=0)&&(index!=-1))
    {
      
        if(result[x][y]==result[x-1][y])
        {
            x=x-1;
           // path[index]=X[x-1];
           // index--;
            //printf("entered loop1: %c",X[x-1]);
            
        }
        else if(result[x][y]==result[x][y-1])
        {
        
            y=y-1;
           // path[index]=Y[y-1];
            //index--;
             //printf("entered loop2: %c",Y[y-1]);
        }
        else 
        {
          path[index]=X[x-1];
           index--;
          x=x-1;
          y=y-1;
         
        }
    }
      printf("\nString: %s ",path);
}
int main()
{
  char str1[] = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA";
  char str2[] = "GTCGTTCGGAATGCCGTTGCTCTGTAAA";
  int len1 = strlen(str1);
  int len2 = strlen(str2);
  
 // printf("Length of Longest Common Sub sequence is = %d\\n", 
  	LongestCommonSubSequence(str1, str2, len1, len2);
 
  return 0;
}
