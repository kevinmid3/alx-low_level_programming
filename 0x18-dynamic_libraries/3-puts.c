#include "main.h"

/**
 * _puts - Prints a string
 * @str: string
 */

void _puts(char *str)
{
	int i = 0;

	for (i = 0; str[i] != '\0'; i++)
	{
		_putchar(str[i]);
	}
	_putchar('\n');
}
