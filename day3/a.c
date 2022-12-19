
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define DICT_LEN 128
#define STR_LEN 128

int priority(char c) {
	if (c <= 'Z') {
		return c - 'A' + 27;
	}
	else if  (c >= 'a') {
		return c - 'a' + 1;
	}
	return -1;
}


int main(int argc, char **argv) {

	FILE *fp;
	char *filepath = argv[1];

	fp = fopen(filepath, "r+");

	if (!fp) {
		exit(1);
	}

	char str[STR_LEN];

	int sum = 0;

	while (fgets(str, STR_LEN, fp) != NULL) {
		
		char *dict = (char*) calloc(DICT_LEN, sizeof(char)); 
		
		int size = strlen(str);
		int half = size >> 1;
		
		for (int i = 0; i < half; i++) {
			dict[str[i] + 0] += 1;
		}

		for (int j = half; j < size; j++) {
			if (dict[str[j] + 0] > 0) {
				sum += priority(str[j]);
				break;
			}
		}

		free(dict);
	}
	printf("%d \n", sum);


	return 0;
}
