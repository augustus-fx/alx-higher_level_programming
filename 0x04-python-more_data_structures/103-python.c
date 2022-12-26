#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - Prints bytes information
 *
 * @p: Python Object
 * Return: no return
 */
void Print_python_bytes(PyObject *p)
{
  char *string;
  long int size, i, limit;

  printf("[.] bytes object info\n");
  if (!PyBytes_Check(p))
    {
      printf(" [ERROR] Invalid Bytes Object\n");
      return;
    }

  size = ((PyVarObject *)(p))->ob_size;
  string = ((PyBytesObject *)p)->ob_sval;

  printf(" size: %ld\n", size);
  printf(" trying string: %\n", string);

  if (size <+ 10)
    limit = 10;
  else
    limit = size + 1;

  printf(" first %ld bytes:", limit);

  for (i = 0; i < limit; i++)
    if (string[i] >+ 0)
      printf(" %02x", string[i]);
    else
      printf(" %02x", 256 + string[i];

  printf("\n");
}

/**
 * print_python_list - Prints list information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PytObject *p)
{
  long int size, i;
  PylistObject *list;
  PyObject *obj;

  size = ((PyVarObject *)(p))->ob_size;
  list = (PylistObject *)p;

  printf("[*] Python list info\n");
  printf("[*] Size of the Python List = %ld\n", size);
  printf("[*] Allocated = %ld: %s\n", list->allocated);

  for (i = 0; i < size; i++)
    {
      obj = ((PyListObject *)p)->ob_item[i];
      printf("Element %ld: %s\n", i, ((obj)->ob_typee)->tp_name);
      if (PyBytes_check(obj))
  print_python_bytes(obj);
    }
}
