class ListTasks:
    # 1. Count Occurrences
    @staticmethod
    def count_occurrences(lst, element):
        return lst.count(element)

    # 2. Sum of Elements
    @staticmethod
    def sum_of_elements(lst):
        return sum(lst)

    # 3. Max Element
    @staticmethod
    def max_element(lst):
        return max(lst) if lst else None

    # 4. Min Element
    @staticmethod
    def min_element(lst):
        return min(lst) if lst else None

    # 5. Check Element
    @staticmethod
    def check_element(lst, element):
        return element in lst

    # 6. First Element
    @staticmethod
    def first_element(lst):
        return lst[0] if lst else None

    # 7. Last Element
    @staticmethod
    def last_element(lst):
        return lst[-1] if lst else None

    # 8. Slice List
    @staticmethod
    def slice_list(lst):
        return lst[:3]

    # 9. Reverse List
    @staticmethod
    def reverse_list(lst):
        return lst[::-1]

    # 10. Sort List
    @staticmethod
    def sort_list(lst):
        return sorted(lst)

    # 11. Remove Duplicates
    @staticmethod
    def remove_duplicates(lst):
        return list(set(lst))

    # 12. Insert Element
    @staticmethod
    def insert_element(lst, index, element):
        lst.insert(index, element)
        return lst

    # 13. Index of Element
    @staticmethod
    def index_of_element(lst, element):
        return lst.index(element) if element in lst else -1

    # 14. Check for Empty List
    @staticmethod
    def check_empty_list(lst):
        return len(lst) == 0

    # 15. Count Even Numbers
    @staticmethod
    def count_even_numbers(lst):
        return sum(1 for num in lst if num % 2 == 0)

    # 16. Count Odd Numbers
    @staticmethod
    def count_odd_numbers(lst):
        return sum(1 for num in lst if num % 2 != 0)

    # 17. Concatenate Lists
    @staticmethod
    def concatenate_lists(lst1, lst2):
        return lst1 + lst2

    # 18. Find Sublist
    @staticmethod
    def find_sublist(lst, sublist):
        sub_len = len(sublist)
        return any(lst[i:i + sub_len] == sublist for i in range(len(lst) - sub_len + 1))

    # 19. Replace Element
    @staticmethod
    def replace_element(lst, old_element, new_element):
        if old_element in lst:
            lst[lst.index(old_element)] = new_element
        return lst

    # 20. Find Second Largest
    @staticmethod
    def find_second_largest(lst):
        unique_lst = list(set(lst))
        unique_lst.sort(reverse=True)
        return unique_lst[1] if len(unique_lst) > 1 else None

    # 21. Find Second Smallest
    @staticmethod
    def find_second_smallest(lst):
        unique_lst = list(set(lst))
        unique_lst.sort()
        return unique_lst[1] if len(unique_lst) > 1 else None

    # 22. Filter Even Numbers
    @staticmethod
    def filter_even_numbers(lst):
        return [num for num in lst if num % 2 == 0]

    # 23. Filter Odd Numbers
    @staticmethod
    def filter_odd_numbers(lst):
        return [num for num in lst if num % 2 != 0]

    # 24. List Length
    @staticmethod
    def list_length(lst):
        return len(lst)

    # 25. Create a Copy
    @staticmethod
    def create_copy(lst):
        return lst.copy()

    # 26. Get Middle Element
    @staticmethod
    def get_middle_element(lst):
        length = len(lst)
        if length % 2 == 0:
            return lst[length // 2 - 1:length // 2 + 1]
        else:
            return lst[length // 2]

    # 27. Find Maximum of Sublist
    @staticmethod
    def find_maximum_of_sublist(lst, start, end):
        return max(lst[start:end]) if lst[start:end] else None

    # 28. Find Minimum of Sublist
    @staticmethod
    def find_minimum_of_sublist(lst, start, end):
        return min(lst[start:end]) if lst[start:end] else None

    # 29. Remove Element by Index
    @staticmethod
    def remove_element_by_index(lst, index):
        if 0 <= index < len(lst):
            lst.pop(index)
        return lst

    # 30. Check if List is Sorted
    @staticmethod
    def check_if_sorted(lst):
        return lst == sorted(lst)

    # 31. Repeat Elements
    @staticmethod
    def repeat_elements(lst, times):
        return [elem for elem in lst for _ in range(times)]

    # 32. Merge and Sort
    @staticmethod
    def merge_and_sort(lst1, lst2):
        return sorted(lst1 + lst2)

    # 33. Find All Indices
    @staticmethod
    def find_all_indices(lst, element):
        return [i for i, x in enumerate(lst) if x == element]

    # 34. Rotate List
    @staticmethod
    def rotate_list(lst, positions):
        return lst[-positions % len(lst):] + lst[:-positions % len(lst)]

    # 35. Create Range List
    @staticmethod
    def create_range_list(start, end):
        return list(range(start, end + 1))

    # 36. Sum of Positive Numbers
    @staticmethod
    def sum_of_positive_numbers(lst):
        return sum(num for num in lst if num > 0)

    # 37. Sum of Negative Numbers
    @staticmethod
    def sum_of_negative_numbers(lst):
        return sum(num for num in lst if num < 0)

    # 38. Check Palindrome
    @staticmethod
    def check_palindrome(lst):
        return lst == lst[::-1]

    # 39. Create Nested List
    @staticmethod
    def create_nested_list(lst, sublist_size):
        return [lst[i:i + sublist_size] for i in range(0, len(lst), sublist_size)]

    # 40. Get Unique Elements in Order
    @staticmethod
    def get_unique_elements_in_order(lst):
        seen = set()
        return [x for x in lst if not (x in seen or seen.add(x))]
