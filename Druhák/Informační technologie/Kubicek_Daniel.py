def bubble_sort(arr, typ_razeni):
    n = len(arr)
    for i in range(n):
        prohodit = False
        for j in range(0, n-i-1):
            if typ_razeni == True:
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    prohodit = True

            if typ_razeni == False:
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


vstupni_pole_hodnot = [64, 34, 25, 12, 22, 11, 90]

print("Seřazené pole pomocí Bubble Sortu:", bubble_sort(vstupni_pole_hodnot, 1))
print("Seřazené pole pomocí Quick Sortu:", quick_sort(vstupni_pole_hodnot, 1))
print("Seřazené pole pomocí Selection Sortu:", selection_sort(vstupni_pole_hodnot, 0))