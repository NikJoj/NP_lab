#include <iostream>
#include <sys/msg.h> 
#include <sys/ipc.h>
#include <string.h>

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

    qu.type = 1; 
    strcpy( qu.message, "message through message queue!");  
  
    // sending message 
    msgsnd( id, &qu, sizeof(qu), 0); 

    cout << "'message through message queue' has been sent" << endl; 
    return 0; 
} 