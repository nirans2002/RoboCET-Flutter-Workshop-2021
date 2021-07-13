#include<iostream>

int main()
{
// declaring variables and getting the array
int Sort[6];
int place=0;
int temp=0;
std::cout<<"Enter numbers to be sorted in the array";
for(int i=0;i<6;i++)
{std::cin>>place;
Sort[i]=place;
}
//sorting array
for (int k=0;k<5;k++)
{int low=Sort[k];
for (int j=k+1;j<=5;j++)
{if (Sort[j]<low)
{Sort[k]=Sort[j];
Sort[j]=low;
low=Sort[k];
}
}
}
//printing sorted array
std::cout<<"Sorted Array is  ";
for(int i=0;i<6;i++)
{std::cout<<Sort[i]<<" ,";
}
return 0;
}



