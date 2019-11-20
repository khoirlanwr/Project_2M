/* 
	Init socket 
	...
*/

#include <stdio.h>
#include <stdlib.h>

#define MAX 100
#define MIN 1

int randGen()
{ return (int)(rand() % (MAX - MIN + 1)) + MIN;  }

int main(int argc, char const *argv[])
{
	
	while(1) 
		printf("rand = %d\n", randGen());


	return 0;
}