#include<iostream>
#include<thread>
#include<time.h>
#include<unistd.h>

using namespace std;

void func(int n)
{
cout<<"thread "<<n<<" is running"<<endl;
//sleep(1);
}

int main()
{
thread t1(func,1);
thread t2(func,2);
thread t3(func,3);

cout<<"hello";
sleep(1);
cout<<"world";
exit(0);
}
