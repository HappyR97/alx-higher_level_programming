#include "lists.h"
#include <stdlib.h>
#include <stddef.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: List head address
 * @number: Node data
 *
 * Return: address of new node, or NULL if failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current;
	listint_t *previous;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	current = *head;
	previous = NULL;
	if (*head == NULL || (*head)->n >= number)
	{
		new->next = *head;
		*head = new;
	}
	else
	{
		while (current != NULL && current->n < number)
		{
			previous = current;
			current = current->next;
		}
	previous->next = new;
	new->next = current;
	}
	return (new);
}
