import random
import time



def create_sorted_list(length):
    """Creates a sorted list of numbers.

    Args:
        length(int): The length of the sorted numbers.

    Returns:
        sorted_list(list): A list of sorted numbers that is the length of the length argument.

    Example:
        >>> create_sorted_list(10)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    sorted_list = []
    for i in range(length):
        sorted_list.append(i)
    return sorted_list


def create_unsorted_list(length):
    """Creates an unsorted list of numbers.

    Args:
        length(int): The length of the unsorted numbers.

    Returns:
        unsorted_list(list): A list of unsorted numbers that is the length of the length argument.

    Example:
        >>> create_unsorted_list(10)
        [0, 6, 7, 8, 3, 5, 1, 9, 2, 4]
    """
    unsorted_list = []
    for i in range(length):
        unsorted_list.append(i)
        random.shuffle(unsorted_list)
    return unsorted_list


def insertion_sort(list):
    """Performs insertion sort on an ordered list and return the sorted list.

    Args:
        list(list): The list of numbers for the item to be sorted.

    Returns:
        (list): The sorted numbers in the list argument.

    Example:
        >>> insertion_sort(create_sorted_list(10))
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            j -= 1
        list[j + 1] = key
    return list


def shell_sort(list):
    """Performs shell sort on an ordered list and return the sorted list.

    Args:
        list(list): The list of numbers for the item to be sorted.

    Returns:
        (list): The sorted numbers in the list argument.


    Example:
        >>> shell_sort(create_sorted_list(10))
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    n = len(list)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = list[i]
            j = 1
            while j >= gap and list[j - gap] > temp:
                j -= gap
            list[j] = temp
        gap //= 2
    return list


def python_sort(list):
    """Performs the python sort method one an ordered list and return the sorted list.

    Args:
        list(list): The list of numbers for the item to be sorted.

    Returns:
        (list): The sorted numbers in the list argument.


    Example:
        >>> python_sort(create_sorted_list(10))
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    return list.sort()


def main():

    """Performs the functions insertion_sort, shell_sort, and python_sort 100 times each in lists the size of
    500, 1000, and 10,000 numbers and shows the average processing time for each function.

    Args:
        None.

    Returns:
        (string): The average time to run each function.

    Example:
        >>> main()
        Insertion sort took 0.3893911838531494 seconds to run, on average
        Shell sort took 1.767711877822876 seconds to run, on average
        Python sort took 0.11959981918334961 seconds to run, on average
    """
    # Test insertion sort with 100 unsorted lists of 500, 1000, and 10000 numbers
    start = time.time()
    for i in range(100):
        insertion_sort(create_sorted_list(100))
    for i in range(100):
        insertion_sort(create_sorted_list(500))
    for i in range(100):
        insertion_sort(create_sorted_list(10000))
    end = time.time()
    total_time = end-start
    print('Insertion sort took {} seconds to run, on average'.format(total_time))

    # Test shell sort with 100 unsorted lists of 500, 1000, and 10000 numbers
    start = time.time()
    for i in range(100):
        shell_sort(create_sorted_list(100))
    for i in range(100):
        shell_sort(create_sorted_list(500))
    for i in range(100):
        shell_sort(create_sorted_list(10000))
    end = time.time()
    total_time = end-start
    print('Shell sort took {} seconds to run, on average'.format(total_time))

    # Test python sort with 100 unsorted lists of 500, 1000, and 10000 numbers
    start = time.time()
    for i in range(100):
        python_sort(create_sorted_list(100))
    for i in range(100):
        python_sort(create_sorted_list(500))
    for i in range(100):
        python_sort(create_sorted_list(10000))
    end = time.time()
    total_time = end-start
    print('Python sort took {} seconds to run, on average'.format(total_time))


if __name__ == "__main__":
    main()