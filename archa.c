#include<stdio.h>
#include<conio.h>
main()
{int i,n,sum=0;
printf("Enter the value for n:");
scanf("%d",&n);
for(i=0;i<=n;i=i+1)
{
    sum=sum+(i*i);
}
printf("sum of squares of first %d natural nos is %d",n,sum);
 }