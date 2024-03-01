typedef struct Result {
    double vysledek;
    char error;
} Result;


Result scitani(int a, int b){
    Result result;
    result.vysledek = a + b;
    result.error = 0;
    return result;
}

Result odcitani(int a, int b){
    Result result;
    result.vysledek = a - b;
    result.error = 0;
    return result;
}

Result nasobeni(int a, int b){
    Result result;
    result.vysledek = a * b;
    result.error = 0;
    return result;
}

Result deleni(int a, int b){
    Result result;
    if (b == 0) return (Result) {0, 1};
    else {
        result.vysledek = a / b;
        result.error = 0;
        return result;
    }
}

Result faktorial(int a){
    Result result;
    if (a < 0) {
        result.vysledek = 0;
        result.error = 1;
        return result;
    }
    else if (a == 1 || a == 0) {
        result.vysledek = 1;
        result.error = 0;
        return result;
    }
    else {
        Result b = faktorial(a - 1);
        result.vysledek = a * b.vysledek;
        result.error = 0;
        return result;
    }
}


Result mocnina(int zaklad, int exponent) {
    Result result;
    if (exponent < 0) {
        result.vysledek = 0;
        result.error = 1;
        return result;
    }

    result.vysledek = 1;
    for (int i = 0; i < exponent; ++i) {
        result.vysledek *= zaklad;
    }

    result.error = 0;
    return result;
}
