import time
import matplotlib.pyplot as plt
import numpy as np

def bubble_sort(arr, typ_razeni):
    n = len(arr)
    for i in range(n):
        prohodit = False
        for j in range(0, n-i-1):
            if typ_razeni:
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    prohodit = True
            else:
                if arr[j] < arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    prohodit = True 
        if not prohodit:
            break
    return arr

def quick_sort(arr, typ_razeni):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        
        if typ_razeni:
            left = [x for x in arr if x < pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x > pivot]
        else:
            left = [x for x in arr if x > pivot]
            middle = [x for x in arr if x == pivot]
            right = [x for x in arr if x < pivot]

        return quick_sort(left, typ_razeni) + middle + quick_sort(right, typ_razeni)

def selection_sort(arr, typ_razeni):
    n = len(arr)
    for i in range(n):
        min_max_index = i
        for j in range(i+1, n):
            if typ_razeni:  # Vzestupné řazení
                if arr[j] < arr[min_max_index]:
                    min_max_index = j
            else:  # Sestupné řazení
                if arr[j] > arr[min_max_index]:
                    min_max_index = j
        arr[i], arr[min_max_index] = arr[min_max_index], arr[i]
    return arr

# Funkce pro měření času
def mereni(alg, arr, typ_razeni, opakovani=5):
    times = []
    for _ in range(opakovani):
        arr_copy = arr.copy()
        start_time = time.time()
        alg(arr_copy, typ_razeni)
        end_time = time.time()
        times.append(end_time - start_time)
    return np.mean(times)

# Generování dat pro datay (best, average, worst case)
def data(alg, sizes, typ_razeni, opakovani=5):
    best = []
    prumer = []
    bad = []
    
    for size in sizes:
        # Nejlepší případ: pole již seřazené
        arr_best = list(range(size))
        best.append(mereni(alg, arr_best, typ_razeni, opakovani))
        
        # Průměrný případ: náhodně generované pole
        arr_avg = np.random.randint(0, 10000, size).tolist()
        prumer.append(mereni(alg, arr_avg, typ_razeni, opakovani))
        
        # Nejhorší případ: pole seřazené v opačném pořadí
        arr_worst = list(range(size, 0, -1))
        bad.append(mereni(alg, arr_worst, typ_razeni, opakovani))
    
    return best, prumer, bad

# Vykreslení dataů
def graf(sizes, best, prumer, bad, sort_name="Sort", approximation="O(n^2)"):
    plt.figure(figsize=(10, 6))

    plt.plot(sizes, best, 'o-', label='best case')
    plt.plot(sizes, prumer, 'o-', label='average case')
    plt.plot(sizes, bad, 'o-', label='worst case')


    if approximation == "O(n^2)":
        plt.plot(sizes, [x**2 for x in sizes], '--', color='blue', label='best approximation (polynom 2. stupně)')
        plt.plot(sizes, [x**2.2 for x in sizes], '--', color='green', label='average approximation (polynom 2.2. stupně)')
        plt.plot(sizes, [x**2.5 for x in sizes], '--', color='purple', label='worst approximation (polynom 2.5. stupně)')
    elif approximation == "O(n log n)":
        plt.plot(sizes, [x * np.log(x) for x in sizes], '--', color='blue', label='best approximation (O(n log n))')
        plt.plot(sizes, [x * np.log(x) for x in sizes], '--', color='green', label='average approximation (O(n log n))')
        plt.plot(sizes, [x**2 for x in sizes], '--', color='purple', label='worst approximation (O(n^2))')

    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Velikost pole')
    plt.ylabel('Průměrný čas (s)')
    plt.title(f'{sort_name} časová složitost v závislosti na velikosti pole')
    plt.legend()
    plt.grid(True)
    plt.show()


sizes = [100, 500, 1000, 5000, 10000]
typ_razeni = False


best_bubble, prumer_bubble, bad_bubble = data(bubble_sort, sizes, typ_razeni)


best_quick, prumer_quick, bad_quick = data(quick_sort, sizes, typ_razeni)


best_selection, prumer_selection, bad_selection = data(selection_sort, sizes, typ_razeni)

# Vykreslení dataů
graf(sizes, best_bubble, prumer_bubble, bad_bubble, sort_name="BubbleSort", approximation="O(n^2)")
graf(sizes, best_quick, prumer_quick, bad_quick, sort_name="QuickSort", approximation="O(n log n)")
graf(sizes, best_selection, prumer_selection, bad_selection, sort_name="SelectionSort", approximation="O(n^2)")
