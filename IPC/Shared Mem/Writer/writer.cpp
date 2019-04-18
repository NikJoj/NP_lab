
#include <iostream> 
#include <sys/ipc.h> 
#include <sys/shm.h> 
#include <string.h> 

using namespace std; 
  
int main() 
{ 
    // generating key 
    key_t key = ftok("cpp_rocks", 39); 
  
    // getting id of shared memory 
    int id = shmget(key,1024,0666|IPC_CREAT); 
  
    // attaching to the shared memory 
    char *message = (char*) shmat( id, (void*) 0, 0 ); 
  
    strcpy( message, "IPC program" );
  
    cout << "message written : " << message << endl;
      
    // detaching from the shared memory  
    shmdt( message ); 
  
    return 0; 
}