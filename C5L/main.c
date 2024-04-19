#include <stdio.h>

float f(float x){
    return x*x - 5;
}

float df(float x){
    return 2 * x;
}

float newton(float xn){
    return xn - (f(xn)/df(xn));
}

float newton_runn(int times, float xn) {
    if(times == 0) {
        return xn;
    }
    
    return newton(newton_runn(times-1, xn));
}

float newton_run(int times, float zelva, float zajic){
    if(times == 0) {
        return 0;
    }

    printf("times - %d\n", times);
    printf("val - %lf\n", zelva);
    if(zelva == zajic) {
        printf("konec\n");
        return zelva;
    } else {
        return newton_run(times-1, newton(zelva),newton(newton(zajic)));    
    }
}


int main() {
    
    /*printf("20? == %lf\n", f(5));
    printf("10 == %lf\n", df(5));
    printf("3 == %lf\n", newton(5));
    printf("%lf\n", newton(4));*/
    
    //printf("%lf", newton_runn(100, 1000));

    printf("%lf", newton_run(1000, 1000, newton(1000)));


}