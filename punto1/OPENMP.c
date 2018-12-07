#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <malloc.h>
#include <omp.h>
#define N 1000
#define PI 3.1415926535
double f(double x);
double _rn(void);
time_t t;



int main(int argc, char ** argv)
{
double candidato;
double r;
int thread_id;
double step = 0.5;
#pragma omp parallel 
{
 int thread_id= omp_get_thread_num();
int thread_count = omp_get_num_threads();

  srand48(thread_id);

double *MC = (double*) calloc(N,sizeof(double));

MC[0] = _rn();
int i = 0;
for(i=1;i<N;i+=1)
{
 candidato = MC[i-1]+(step)*(_rn()-0.5);
 r = f(candidato)/f(MC[i-1]);
 r = fmin(1,r);
 if(_rn() < r){
  MC[i] = candidato;   
 }
 else{
 MC[i] = MC[i-1];   
 }
}

char *file = (char *) malloc(sizeof(char)*100);
thread_id= omp_get_thread_num();
sprintf(file, "sample%d.txt", thread_id);
FILE *output = fopen(file, "w+");
for(int j=0;j<N;j+=1) {
          fprintf(output, "%f\n",MC[j]);
			}
	fclose(output);

}

return 0;
}


double f(double x)
{
	int sigma=1;
 return pow(2*PI,-1/2)*exp(-x*x/2.0*sigma);   
}
double _rn(void)
{
    return (double) rand()/(RAND_MAX*1.0);
}



