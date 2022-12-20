
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
	char str2[STR_LEN];
	char str3[STR_LEN];
	
	int sum = 0;

	while (fgets(str, STR_LEN, fp) != NULL) {

		char *res = fgets(str2, STR_LEN, fp);
		char *res2 = fgets(str3, STR_LEN, fp);

		if (res == NULL || res2 == NULL) {
			exit(1);
		}
		
		char *dict = (char*) calloc(2 * DICT_LEN, sizeof(char)); 
		
		size_t size1 = strlen(str);
		size_t size2 = strlen(str2);
		size_t size3 = strlen(str3);


		for (size_t i = 0; i < size1; i++) {
			dict[str[i] + 0] += 1;
		}
		
		for (size_t i = 0; i < size2; i++) {
			dict[2 * (str2[i] + 0)] += 1;
		}

		for (size_t i = 0; i < size3; i++) {
			if (dict[str3[i] + 0] > 0 && dict[2 * (str3[i] + 0)] > 0) {
				sum += priority(str3[i]);
				break;
			}
		}

		free(dict);
	}
	printf("%d \n", sum);


	return 0;
}
