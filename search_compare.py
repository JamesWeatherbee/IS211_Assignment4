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


def sequential_search(list, item):
    """Performs a sequential search for an item on an ordered list and returns a tuple with the boolean True and the
    position of the item on the list.

    Args:
        list(list): The list of numbers for the item to be searched for.
        item(int): The number that is to be searched for in the list.

    Returns:
        Tuple: True boolean and the item position if it is in the list.
        Comment: States that the item is not in the list.

    Example:
        >>> sequential_search([1,2,3,4,5], 5)
        (True, 4)
        >>> sequential_search([1,2,3,4,5], 6)
        6 not in list.
    """
    position = 0
    while position < len(list):
        if list[position] == item:
            return True, position
        position = position + 1
    return '{} not in list.'.format(item)


def ordered_sequential_search(list, item):
    """Performs an ordered sequential search for an item on an ordered list and returns a tuple with the boolean True and the
    position of the item on the list.

    Args:
        list(list): The list of numbers for the item to be searched for.
        item(int): The number that is to be searched for in the list.

    Returns:
        Tuple: True boolean and the item position if it is in the list.
        Comment: States that the item is not in the list.

        Example:
        >>> ordered_sequential_search([1,2,3,4,5], 5)
        (True, 4)
        >>> ordered_sequential_search([1,2,3,4,5], 6)
        6 not in list.
    """
    position = 0
    while position < len(list):
        if list[position] == item:
            return True, position
        position = position + 1
    return '{} not in list.'.format(item)


def binary_search_iterative(list, item):
    """Performs a iterative binary search for an item on an ordered list and returns a tuple with the boolean True and
    the position of the item on the list.

    Args:
        list(list): The list of numbers for the item to be searched for.
        item(int): The number that is to be searched for in the list.

    Returns:
        Tuple: True boolean and the item position if it is in the list.
        Comment: States that the item is not in the list.

        Example:
        >>> binary_search_iterative([1,2,3,4,5], 5)
        (True, 4)
        >>> binary_search_iterative([1,2,3,4,5], 6)
        6 not in list.
    """
    low = 0
    high = len(list) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if list[mid] < item:
            low = mid + 1
        elif list[mid] > item:
            high = mid - 1
        else:
            return True, mid
    return '{} not in list.'.format(item)


def binary_search_recursive(list, low, high, item):
    """Performs a recursvie binary search for an item on an ordered list and returns a tuple with the boolean True and
    the position of the item on the list.

    Args:
        list(list): The list of numbers for the item to be searched for.
        low(int): The lower limit of the list
        high(int): The upper limit of the list.
        item(int): The number that is to be searched for in the list.

    Returns:
        Tuple: True boolean and the item position if it is in the list.
        Comment: States that the item is not in the list.

        Example:
        >>> binary_search_recursive([1,2,3,4,5], 0, 5, 5)
        (True, 4)
        >>> binary_search_recursive([1,2,3,4,5], 0, 5, 6)
        6 not in list.
    """
    if high >= low:
        mid = (high + low) // 2
        if list[mid] == item:
            return True, mid
        elif list[mid] > item:
            return binary_search_recursive(list, low, mid - 1, item)
        else:
            return binary_search_recursive(list, mid + 1, high, item)
    return '{} not in list.'.format(item)


def main():
    """Performs the functions sequential_search, ordered_sequential_search, binary_search_iterative, and
    binary_search_recursive to search for -1 100 times each in lists the size of 500, 1000, and 10,000 numbers and
    shows the average processing time for each function.

    Args:
        None.

    Returns:
        (string): The average time to run each function.

    Example:
        >>> main()
        Sequential Search took 0.3726987838745117 seconds to run, on average
        Ordered sequential search took 0.42754292488098145 seconds to run, on average
        Binary iterative search search took 0.12359499931335449 seconds to run, on average
        Binary iterative search search took 0.11751484870910645 seconds to run, on average

    """
    # Test sequential search with 100 unsorted lists of 500, 1000, and 10000 numbers
    start = time.time()
    for i in range(100):
        sequential_search(create_sorted_list(500), -1)
    for i in range(100):
        sequential_search(create_sorted_list(1000), -1)
    for i in range(100):
        sequential_search(create_sorted_list(10000), -1)
    end = time.time()
    total_time = end-start
    print('Sequential Search took {} seconds to run, on average'.format(total_time))

    # Test ordered sequential search with 100 sorted lists of 500, 1000, and 10000 numbers
    start = time.time()
    for i in range(100):
        ordered_sequential_search(create_sorted_list(500), -1)
    for i in range(100):
        ordered_sequential_search(create_sorted_list(1000), -1)
    for i in range(100):
        ordered_sequential_search(create_sorted_list(10000), -1)
    end = time.time()
    total_time = end-start
    print('Ordered sequential search took {} seconds to run, on average'.format(total_time))

    # Test binary iterative search with 100 sorted lists of 500, 1000, and 10000 numbers
    start = time.time()
    for i in range(100):
        binary_search_iterative(create_sorted_list(500), -1)
    for i in range(100):
        binary_search_iterative(create_sorted_list(1000), -1)
    for i in range(100):
        binary_search_iterative(create_sorted_list(10000), -1)
    end = time.time()
    total_time = end-start
    print('Binary iterative search search took {} seconds to run, on average'.format(total_time))

    # Test binary recursive search with 100 sorted lists of 500, 1000, and 10000 numbers
    start = time.time()
    for i in range(100):
        binary_search_recursive(create_sorted_list(500), 1, 500, -1)
    for i in range(100):
        binary_search_recursive(create_sorted_list(1000), 1, 1000, -1)
    for i in range(100):
        binary_search_recursive(create_sorted_list(10000), 1, 10000, -1)
    end = time.time()
    total_time = end-start
    print('Binary iterative search search took {} seconds to run, on average'.format(total_time))


if __name__ == "__main__":
    main()