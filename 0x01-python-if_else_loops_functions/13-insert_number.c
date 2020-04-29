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

	while (current && current->next)
	{
		if (number > current->n)
		{
			previous = current;
			current = current->next;
		}
		else
		{
			node->n = number;
			node->next = previous->next;
			previous->next = node;
			return (node);
		}
	}
	return (NULL);
}
