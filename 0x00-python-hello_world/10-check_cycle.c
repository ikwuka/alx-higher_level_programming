#include "lists.h"
/**
 * check_cycle -linked list cycle
 * @list: the pointer to the struct
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *a = list;
	listint_t *b = list;

	if (list == NULL)
	{
		return (0);
	}

	b = b->next;

	while (a != NULL && b != NULL && b->next != NULL)
	{
		if (b == a)
		{
			return (1);
		}
		b = b->next->next;
		a = a->next;
	}
	return (0);
}
