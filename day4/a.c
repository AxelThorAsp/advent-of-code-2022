
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
		if (a >= c && b <= d) {
			sum++;
			continue;
		}
		if (c >= a && d <= b) {
			sum++;
		} 
	}

	fclose(fp);
	printf("%d \n", sum);
	return 0;
}
