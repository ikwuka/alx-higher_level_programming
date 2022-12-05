#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints some basic info about Python lists
 * @p: pointer to the Python struct
 */

void print_python_list_info(PyObject *p)
{
	unsigned int ind;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

	for (ind = 0; ind < PyList_Size(p); ind++)
		printf("Element %d: %s\n", ind, Py_TYPE(PyList_GetItem(p, ind))->tp_name);
}
