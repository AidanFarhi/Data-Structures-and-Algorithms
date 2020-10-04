
def heaps_algorithm(arr):

    output = []

    def swap(swap_arr, i, j):
        t = swap_arr[i]
        swap_arr[i] = swap_arr[j]
        swap_arr[j] = swap_arr[i]
    
    def generate(heap_arr, length):
        if length == 0:
            output.append(heap_arr[:])
            return

        generate(heap_arr, length - 1)
        for i in range(length - 1):
            if length % 2 == 0:
                swap(heap_arr, i, length - 1)
            else:
                swap(heap_arr, 0, length - 1)
            generate(heap_arr, length - 1)
    
    generate(arr[:], len(arr))
    return output
        