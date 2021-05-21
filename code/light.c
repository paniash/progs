#include <stdio.h>

const double c = 299792458.0;

double light_time(double distance){
	double t = 0.0;

	t = distance/c;
	return t;
}

int main(){
	double ttime;
	ttime = light_time(299792458);
	printf("%f", ttime);
	return 0;
}
