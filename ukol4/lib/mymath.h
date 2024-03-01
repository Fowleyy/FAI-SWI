int faktorial(int n) {
    if (n <= 1) {
        return 1;
    } else {
        return n * faktorial(n - 1);
    }
}

int mocnina(int a, int n){
if ((a == 1)||(n==0)){   
    return 1;
}
else{
    return a * mocnina(a,n-1);
}
}

int fibo(int n){
    if (n<=1){
        return n;
    }

    else{
        return fibo(n-1) + fibo(n-2);
    }
}