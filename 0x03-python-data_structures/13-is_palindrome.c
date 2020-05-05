#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: listint_t linked list head
 * Return: 1 if it is a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *h = *head;
	int i = 0, j = 0, *nums = NULL;

	if (!*head || !(*head)->next)
		return (1);

	for (j = 0; h; j++)
		h = h->next;

	nums = malloc(sizeof(int) * j);
	h = *head;

	for (i = 0; h; i++)
	{
		nums[i] = h->n;
		h = h->next;
	}

	for (i = 0; i < j / 2; i++)
	{
		if (nums[i] != nums[j - 1 - i])
		{
			free(nums);
			return (0);
		}
	}

	free(nums);
	return (1);
}