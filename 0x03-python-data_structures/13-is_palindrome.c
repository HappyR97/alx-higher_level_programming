#include "lists.h"

/**
 * is_palindrome - Checks if linked list is a palindrome
 * @head: pointer to pointer of first node of a list
 *
 * Return: 0 if not palindrome, 1 if palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *ptr;
	int size = 1, i, j;

	ptr = *head;
	while (ptr->next != NULL)
	{
		ptr = ptr->next;
		size++;
	}

	int values[size];

	ptr = *head;
	for (i = 0; ptr != NULL; i++)
	{
		values[i] = ptr->n;
		ptr = ptr->next;
	}

	for (i = 0, j = size - 1; i < size / 2; i++, j--)
		if (values[i] != values[j])
			return (0);
	return (1);
}
