#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/*
 * Check argument number
 */
void argCheck (int arg)
{
	if (arg != 2) {
		printf("\n\tUsage :    ./reverse    [Input String]\n\n");
		exit(1);
	}
}



/*
 * Swap with char type
 */
void swap_ch (char *a, char *b)
{
	*a ^= *b;
	*b ^= *a;
	*a ^= *b;
}



/*
 * Read the input address string (till '\0'), and reverse the character in place
 */

// version 1 : only sort in place, but use no recursive
char* reverse_v1 (char *s)
{
	if (*s == '\0') return;

	int string_length = strlen(s);
	int cnt;

	for (cnt=0; cnt<(string_length/2); cnt++)
		swap_ch (&s[cnt], &s[string_length-cnt-1]);
}


// version 2 : sort in place, recursive, but use no return value to process reverse step
char* reverse_v2 (char *s)
{
	if (*(s+1) == '\0') return;

	int string_length = strlen(s);
	char chtmp = *s;

	swap_ch (s, (s+string_length-1));
	*(s+string_length-1) = '\0';

	reverse_v2 (s+1);

	*(s+string_length-1) = chtmp;

	return s;
}



/*
 * Main function
 */
int main (int argc, char* argv[])
{
	// Check Argument, exit program if error
	argCheck (argc);


	// Variable declaration and read in argv[1] as an input string
	char *input_string;
	input_string = (char*) malloc (sizeof(char)*strlen(argv[1]));
	strcpy (input_string, argv[1]);


	printf ("\nOriginal String :  %s\n", input_string);

	//reverse_v1 (input_string);
	reverse_v2 (input_string);

	printf ("\nReverse String :  %s\n", input_string);


	reverse_v2( reverse_v2 (reverse_v2(input_string)));

	printf ("\nReverse Back String (To origin) :  %s\n", input_string);


	free (input_string);
	return 0;
}

