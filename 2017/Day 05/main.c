#include <string.h>
#include <stdlib.h>
#include <stdio.h>

#define dynstep(x) x >= 3 ? x-- : x++
#define allocate (short*) malloc(array_size);
#define array_size sizeof(short) * length

int main(int argc, char *argv[])
{
  int s1 = 0, s2 = 0, ptr, length = 0;
  FILE *fp = fopen("input.txt", "r");
  if (fp == NULL)
    exit(EXIT_FAILURE);
  // Count Lines
  while (!feof(fp))
    if (fgetc(fp) == '\n')
      ++length;
  // Begin Tape Read
  short* init = allocate;
  fseek(fp, 0, SEEK_SET);
  for(int i = 0; i < length; i++)
    fscanf(fp, "%hi", i+init);
  fclose(fp); short* last = allocate;
  memcpy(last, init, array_size);
  // Solve Part 1
  for(ptr = 0; ptr < length; s1++)
    ptr += init[ptr]++;
  printf("Silver: %d\n", s1);
  // Solve Part 2
  for(ptr = 0; ptr < length; s2++)
    ptr += dynstep(last[ptr]);
  printf("Gold: %d\n", s2);
    free(init); free(last);
  return 0;
}
