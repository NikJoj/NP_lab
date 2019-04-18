#include <iostream>
#include <unistd.h>
#include <thread>
#include <mutex>

using namespace std;

mutex read_lock, wall, qu, write_lock, trial;
int rdcount, wrcount;

void reader( int n ) {
    do {
        while( !qu.try_lock() );
        while( !read_lock.try_lock() );
        rdcount++;
        if( rdcount == 1 )
            while( !wall.try_lock() );        
        read_lock.unlock();        
        qu.unlock();
        cout << "reader " << n << " is reading...\n";
        sleep(1);
        cout << "reader " << n << " finished reading.\n";        
        while( !read_lock.try_lock() );        
        rdcount--;
        if( rdcount == 0 )
            wall.unlock();
        read_lock.unlock();
        sleep(1);
    } while( true );
}

void writer( int n ) {
    do {
        while( !qu.try_lock() );
        while( !write_lock.try_lock() );
        wrcount++;
        if( wrcount == 1 )
            while( !wall.try_lock() );        
        write_lock.unlock();        
        qu.unlock();
        while( !trial.try_lock() );
        cout << "writer " << n << " is writiing...\n";
        sleep(1.5);
        cout << "writer " << n << " finished writing.\n";        
        trial.unlock();
        while( !write_lock.try_lock() );        
        wrcount--;
        if( wrcount == 0 )
            wall.unlock();
        write_lock.unlock();
        sleep(1.5);
    }while( true );
}

int main() {
    rdcount = wrcount = 0;
    thread w1( writer, 1 );
    thread r1( reader, 1 );
    thread r2( reader, 2 );    
    thread w2( writer, 2 );
    thread r3( reader, 3 );
    r1.join();
    r2.join();
    w1.join();
    w2.join();
    r3.join();    
    return 0;
}