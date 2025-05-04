#include <stdio.h>

int main()
{
  int n = 26;
  int arr[n];
  char *ptr = arr;
  for (int i = 0; i < n; i++)
  {
    *(ptr + i) = (char)(i + 65);
  }
  for (int i = 0; i < n; i++)
  {

    printf("%c ", *(ptr + i));
  }
  return 0;
}