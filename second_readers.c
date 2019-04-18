#include<stdio.h>
#include<pthread.h>
#include<semaphore.h>
#include<unistd.h>
#include<stdlib.h>
sem_t rmutex ;
sem_t wmutex ;
sem_t mutex_1 ;
sem_t mutex_2 ;
sem_t mutex_3 ;
int readcount , writecount ;
int c =0;
int z =0;
void * reader ( int *x ){
int p=++c ;
sem_wait (&mutex_3 ) ;
sem_wait (&rmutex ) ;
sem_wait (&mutex_1 ) ;
readcount++;
if ( readcount == 1 ){
sem_wait (&wmutex ) ;
}
sem_post (&mutex_1 ) ;
sem_post (&rmutex ) ;
sem_post (&mutex_3 ) ;
printf ( ”\nReading %d Started \n” , p ) ;
sem_wait (&mutex_1 ) ;
printf ( ”\nReading %d completed \n” , p ) ;
readcount−−;
if ( readcount == 0 ){
sem_post (&wmutex ) ;
}
sem_post (&mutex_1 ) ;
}
void * writer ( ) {
int p=++z ;
sem_wait (&mutex_2 ) ;
writecount++;
if ( writecount == 1 ){
sem_wait (&rmutex ) ;
}
sem_post (&mutex_2 ) ;
sem_wait (&wmutex ) ;
printf ( ”\nWriting %d Started \n” , p ) ;
sem_post (&wmutex ) ;
sem_wait (&mutex_2 ) ;
writecount−−;
printf ( ”\nWriting %d Completed\n” , p ) ;
if ( writecount == 0 ){
sem_post (&rmutex ) ;
}
sem_post (&mutex_2 ) ;
}
void main ( ) {
sem_init (&rmutex , 0 , 1 ) ;
sem_init (&wmutex , 0 , 1 ) ;
sem_init (&mutex_1 , 0 , 1 ) ;
sem_init (&mutex_2 , 0 , 1 ) ;
sem_init (&mutex_3 , 0 , 1 ) ;
pthread_t t[ 5 ] ;
for ( int i =0; i <6; i++){
if ( i%2 == 0 ){
pthread_create (&t[ i ] ,NULL, reader ,NULL ) ;
}
else {
pthread_create (&t[i] ,NULL, writer ,NULL ) ;
}
}
}