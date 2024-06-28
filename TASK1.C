#include<stdio.h>


void converter()
{
	float celsius,fahrenheit,kelvin;
	printf("\nenter value of celsius :-");
	scanf("%f",&celsius);
	fahrenheit = (celsius * 9.0 / 5.0) + 32.0;
	kelvin = celsius + 273.15;

	printf("\nfahrenheit is %.2f: ",fahrenheit);
	printf("\nkelvin is %.2f",kelvin);

}

void main()
{
	int ch;
	clrscr();

	printf("\n<---- temprature converter ---->");

	printf("\n01 to convert celsius to fahrenheit and kelvin.");
	printf("\n02 to exit.");

	do
	 {
	  printf("\nenter your choice(1,2) :- ");
	  scanf("\n%d",&ch);

	  if(ch == 0)
	  {
	    printf("enter valid choice..");
	  }
	  else if(ch >= 3)
	  {
	    printf("enter valid choice..");
	  }

	     switch(ch)
	     {
		case 1:  // calculate fahrenheit and kelvin
		converter();
		break;


	    case 2: //exit
		exit(0);
		break;
	      }
	   } while(ch != 2);


	getch();
}



