#include<iostream>
#include<mutex>
#include<thread>
#include<stdlib.h>
#include<unistd.h>
#include<time.h>



using namespace std;

mutex m,alock;
int a;

//if a is 0 then 5,10
//if a is 1 then 10,20
//if a is 2 then 5,20

void eat()
{
	while(1)
	{

		while(!alock.try_lock());
		 
		a = rand();
		a = (a%10)/4;
		//cout<<a<<"is value of a"<<endl;
	
		if (a == 0)
		{
			while(!m.try_lock());
			cout<<"Professor with 20 is eating."<<endl;
			//sleep(1);
			cout<<"Professor with 20 finished eating."<<endl;
			//sleep(1);
			m.unlock();
		}	
		if (a == 1)
		{
			while(!m.try_lock());
			cout<<"Professor with 5 is eating."<<endl;
			//sleep(1);
			cout<<"Professor with 5 finished eating."<<endl;
			//sleep(1);		
			m.unlock();
		}
		if (a == 2)
		{
			while(!m.try_lock());
			cout<<"Professor with 10 is eating."<<endl;
			//sleep(1);
			cout<<"Professor with 10 finished eating."<<endl;
			//sleep(1);		
			m.unlock();
		}
		alock.unlock();

	}
}

int main()
{

	thread e1(eat);
	thread e2(eat);
	thread e3(eat);

	exit(0);
	
}
