#include<stdio.h>
#include<conio.h>
#include<time.h>

int main()
{
      int random,guess,count=0;
      clrscr();
      srand(time(0));
      random = rand() % 5 + 1;

      printf("welcome to guessing game..");

      do{
      printf("\nenter your guess number(0-5)..");
      scanf("%d",&guess);
      count++;

      if(guess > random)
      { printf("\nyour guess is too high! try again..");  }

      else if(guess < random)
      { printf("\nyour guess is too low! try again.."); }

      else
      { printf("\ncongratulation! you win guess..");
	printf("\nit tooks you %d attempts to win the game..",count);
      }
      }while(guess != random);
      getch();
}