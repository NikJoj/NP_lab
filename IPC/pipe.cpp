#include <iostream>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

using namespace std;

int main() {

    char toChild[] = "CET tvm";
    char toParent[] = " sem 6";

    int comm[2];
    if( pipe(comm) < 0 ) {
        cout << "\nerror creating pipe\n";
        return 1;        
    }

    int pid = fork();
    if( pid < 0 ) {
        cout << "\nerror creating another process\n";
        return 1;        
    }

    /*      child section       */
    if( !pid ) {
        char fromParent[17];        
        read( comm[0], fromParent, 7 );
        strcat( fromParent, toParent );
        write( comm[1], fromParent, 14 );
        return 0;
    }

    /*      parent section      */
    cout << "sending message to child : " << toChild << endl;
    write( comm[1], toChild, 7 );
    wait( NULL );
    char fromChild[15];
    read( comm[0], fromChild, 14 );
    cout << "received message from child : " << fromChild << endl;

    return 0;
}