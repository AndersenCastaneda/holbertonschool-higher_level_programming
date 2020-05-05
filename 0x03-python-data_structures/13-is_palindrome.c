#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: listint_t linked list head
 * Return: 1 if it is a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *h = *head;
	size_t i, j, *k = NULL;

	if (!*head || !(*head)->next)
		return (1);

	for (j = 0; h->next; j++)
		h = h->next;

	k = malloc(sizeof(int) * j);
	h = *head;

	for (i = 0; h; i++)
	{
		k[i] = h->n;
		h = h->next;
	}

	for (i = 0; i < j; i++, j--)
	{
		if (k[i] != k[j])
		{
			free(k);
			return (0);
		}
	}

	free(k);
	return (1);
}