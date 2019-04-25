#include<unistd.h>
#include<time.h>
#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
int a;
while(1)
{
abc:
a = rand();
if (a%10!=0)
a = (a%10)/4;
else
goto abc;
cout<<a<<endl;
sleep(1);
}

exit(0);
}
