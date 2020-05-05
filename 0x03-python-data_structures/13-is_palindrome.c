#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: listint_t linked list head
 * Return: 1 if it is a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *h = *head, *e = NULL;
	size_t i = 0, j, k;

	if (!*head || !(*head)->next)
		return (1);

	for (j = 0; h->next; j++)
		h = h->next;

	h = *head;
	while (i < j)
	{
		e = h;
		for (k = i; k < j; k++)
			e = e->next;

		if (h->n == e->n)
		{
			i++;
			j--;
			h = h->next;
		}
		else
			return (0);
	}

	return (1);
}