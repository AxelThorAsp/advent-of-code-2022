
#include <stdio.h>
#include <stdlib.h>


int score(char a, char b) {
    if (a == 'A') {
        if (b == 'X') return 0 + 1;
        if (b == 'Y') return 3 + 2;
        if (b == 'Z') return 6 + 3;
    }
    else if (a == 'B') {
        if (b == 'X') return 0 + 1;
        if (b == 'Y') return 3 + 2;
        if (b == 'Z') return 6 + 3;
    }
    else if (a == 'C') {
        if (b == 'X') return 6 + 1;
        if (b == 'Y') return 0 + 2;
        if (b == 'Z') return 3 + 3;
    }
    return 0;
}


int main (int argc, char **argv) {
   char a, b;
   FILE *fp;
   char *filepath = argv[1];
   int sum = 0;

   fp = fopen(filepath, "r+");

   if (!fp) {
       exit(1);
   }
   while(fscanf(fp, " %c %c", &a, &b) != EOF) {
       sum += score(a,b);
   }

   printf("%d\n",sum);

   fclose(fp);
   return(0);
}
