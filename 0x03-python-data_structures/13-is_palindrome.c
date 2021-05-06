#include "lists.h"

int palindrome(listint_t *head, listint_t *node, int index)
{
	int isPalindrome, current;

	if (node == NULL)
		return (index);

	isPalindrome = palindrome(head, node->next, index + 1);

	if (!isPalindrome)
		return (0);
	current = isPalindrome - index;
	for (; current > 1; current--)
		head = head->next;

	if (head->n == node->n)
		return (isPalindrome);
	return (0);
}

int is_palindrome(listint_t **head)
{
	if (!head || !*head)
		return (0);

	return (palindrome(*head, *head, 0) ? 1 : 0);
}
