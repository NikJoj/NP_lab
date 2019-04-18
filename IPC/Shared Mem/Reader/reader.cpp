
#include <iostream> 
#include <sys/ipc.h> 
#include <sys/shm.h> 

using namespace std; 
  
int main() 
{ // generating key 
    key_t key = ftok("cpp_rocks", 39); 
  
    // getting id of shared memory 
    int id = shmget(key,1024,0666|IPC_CREAT); 
  
    // attaching to the shared memory 
    char *message = (char*) shmat( id, (void*) 0, 0 ); 
  
    cout << "message read : " << message << endl; 
      
    // detaching from the shared memory  
    shmdt( message ); 
    
    // destroying the shared memory 
    shmctl(id,IPC_RMID,NULL); 
     
    return 0; 
} 