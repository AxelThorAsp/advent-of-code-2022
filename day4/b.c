
#include <stdio.h>
#include <stdlib.h>
#include <string.h>





int main(int argc, char **argv) {
	FILE *fp;
	char *filepath = argv[1];

	fp = fopen(filepath, "r+");

	if (!fp) {
		exit(1);
	}
	
	int sum = 0;
	
	int a, b, c, d;
	
	while (fscanf(fp, "%d-%d,%d-%d", &a, &b, &c, &d) != EOF) {
		for (int i = a; i <=b; i++) {
			if (i >= c && i <= d) {
				sum++;
				break;
			}
		}

	}

	fclose(fp);
	printf("%d \n", sum);
	return 0;
}
