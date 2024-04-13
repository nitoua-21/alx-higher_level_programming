#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <Python.h>

/**
* print_python_string -  prints Python strings.
*
* @p: PyObject
*
*/
void print_python_string(PyObject *p)
{
	PyASCIIObject *asciio;
	PyCompactUnicodeObject *comp;
	PyVarObject *var;
	Py_ssize_t length;
	const char *str;

	int i;

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	asciio = (PyASCIIObject *)p;
	comp = (PyCompactUnicodeObject *)p;
	var = (PyVarObject *)p;
	length = var->ob_size;

	if (comp->state.ascii)
	{
		printf("  type: compact ascii\n");
		str = (const char *)asciio->data;
	}
	else
	{
		printf("  type: compact unicode object\n");
		str = (const char *)comp->data;
	}

	printf("  length: %ld\n", length);

	printf("  value: %s\n", str);
}
