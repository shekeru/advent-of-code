#include <stdlib.h>
#include <stdio.h>

typedef struct list {
  struct list* next;
  int value;
  int sum;
} list;

list* head = NULL;
list* last = NULL;
list* stab = NULL;
int n_count = 0;

void add(int val)
{
  list* new = (list*) malloc(sizeof(list));
  if(last){
    new->sum = val+last->sum;
    last->next = new;
    last = new;
  } else if(head){
    new->sum = val+head->sum;
    head->next = new;
    last = new;
  } else {
    new->sum = val;
    head = new;
  }
  new->value = val;
}

void read_file()
{
  char buffer[256]; FILE* fd
    = fopen("input.txt", "rb");
  while(fgets(buffer, sizeof buffer, fd))
    add(strtol(buffer, (char**) &buffer[256], 10));
  fclose(fd); stab = last;
}

int forwards(list* curr)
{//Why is this function so slow...
  if(!curr->sum)
    return curr->sum;
  for(list* cmp = head; cmp != curr; cmp = cmp->next)
    if(curr->sum == cmp->sum)
      return curr->sum;
  if(curr == last) {
    for(list* t = head; t != stab; t=t->next)
      add(t->value); add(stab->value);
  } return forwards(curr->next);
}

int main()
{
  read_file(); printf("part 1: %d\n", stab->sum);
  printf("part 2: %d\n", forwards(head));
  return 0;
}
