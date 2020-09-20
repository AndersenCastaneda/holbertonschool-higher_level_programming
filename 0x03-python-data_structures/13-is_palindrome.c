#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: listint_t linked list head
 * Return: 1 if it is a palindrome, otherwise 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *hd = *head;
	int i = 0, j = 0, flag = 1, *nums = NULL;

	if (!hd || !hd->next)
		return (flag);

	for (j = 0; hd; j++)
		hd = hd->next;

	nums = malloc(j * 4);
	if (!nums)
		return (0);
	hd = *head;

	for (i = 0; hd; i++)
	{
		nums[i] = hd->n;
		hd = hd->next;
	}

	j -= 1;
	for (i = 0; i <= j; i++, j--)
	{
		if (nums[i] != nums[j])
		{
			flag = 0;
			break;
		}
	}

	free(nums);
	return (flag);
}
