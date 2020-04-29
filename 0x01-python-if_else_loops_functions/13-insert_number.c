#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *previous;
	listint_t *node = malloc(sizeof(listint_t));

	if (!head || !node)
		return (NULL);

	node->n = number;
	if (!*head || (*head)->n > number)
	{
		node->next = *head;
		return (*head = node);
	}
	else
	{
		while (current && number > current->n)
		{
			previous = current;
			current = current->next;	
		}
		previous->next = node;
		node->next = current;
	}

	return (node);
}
