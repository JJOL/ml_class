
#include <stdio.h>

int main()
{
  FILE * file = fopen("estados_pob_f.csv", "r");
  //FILE * file = fopen("estados_delincuencia", "r");
  if (file == 0) return 0;

  char c;
  do {
  c = fgetc(file);
  printf("%c => %d\n", c, (int)c);
  } while (c != EOF);

  fclose(file);

return 0;
}
