
#include <iostream>
#include <sys/msg.h> 
#include <sys/ipc.h>

using namespace std;
 
struct mesg_buffer { 
    long type; 
    char message[100]; 
} qu; 
  
int main() 
{ 
    key_t key; 
    int id; 
  
    // generating key 
    key = ftok("cpp_rocks", 39); 
  
    // creating message queue 
    id = msgget(key, 0666 | IPC_CREAT);

    // receiving message 
    msgrcv( id, &qu, sizeof(qu), 1, 0); 

    cout << qu.message << endl; 

    // destroying the message queue 
    msgctl( id, IPC_RMID, NULL ); 

    return 0; 
}     