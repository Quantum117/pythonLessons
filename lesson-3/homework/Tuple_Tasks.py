class TupleTasks:
    # 1. Count Occurrences
    @staticmethod
    def count_occurrences(tpl, element):
        return tpl.count(element)

    # 2. Max Element
    @staticmethod
    def max_element(tpl):
        return max(tpl) if tpl else None

    # 3. Min Element
    @staticmethod
    def min_element(tpl):
        return min(tpl) if tpl else None

    # 4. Check Element
    @staticmethod
    def check_element(tpl, element):
        return element in tpl

    # 5. First Element
    @staticmethod
    def first_element(tpl):
        return tpl[0] if tpl else None

    # 6. Last Element
    @staticmethod
    def last_element(tpl):
        return tpl[-1] if tpl else None

    # 7. Tuple Length
    @staticmethod
    def tuple_length(tpl):
        return len(tpl)

    # 8. Slice Tuple
    @staticmethod
    def slice_tuple(tpl):
        return tpl[:3]

    # 9. Concatenate Tuples
    @staticmethod
    def concatenate_tuples(tpl1, tpl2):
        return tpl1 + tpl2

    # 10. Check if Tuple is Empty
    @staticmethod
    def check_empty_tuple(tpl):
        return len(tpl) == 0

    # 11. Get All Indices of Element
    @staticmethod
    def get_all_indices_of_element(tpl, element):
        return [i for i, x in enumerate(tpl) if x == element]

    # 12. Find Second Largest
    @staticmethod
    def find_second_largest(tpl):
        unique_tpl = sorted(set(tpl), reverse=True)
        return unique_tpl[1] if len(unique_tpl) > 1 else None

    # 13. Find Second Smallest
    @staticmethod
    def find_second_smallest(tpl):
        unique_tpl = sorted(set(tpl))
        return unique_tpl[1] if len(unique_tpl) > 1 else None

    # 14. Create a Single Element Tuple
    @staticmethod
    def create_single_element_tuple(element):
        return (element,)

    # 15. Convert List to Tuple
    @staticmethod
    def convert_list_to_tuple(lst):
        return tuple(lst)

    # 16. Check if Tuple is Sorted
    @staticmethod
    def check_if_sorted(tpl):
        return tpl == tuple(sorted(tpl))

    # 17. Find Maximum of Subtuple
    @staticmethod
    def find_maximum_of_subtuple(tpl, start, end):
        return max(tpl[start:end]) if tpl[start:end] else None

    # 18. Find Minimum of Subtuple
    @staticmethod
    def find_minimum_of_subtuple(tpl, start, end):
        return min(tpl[start:end]) if tpl[start:end] else None

    # 19. Remove Element by Value
    @staticmethod
    def remove_element_by_value(tpl, element):
        tpl_list = list(tpl)
        if element in tpl_list:
            tpl_list.remove(element)
        return tuple(tpl_list)

    # 20. Create Nested Tuple
    @staticmethod
    def create_nested_tuple(tpl, subtuple_size):
        return tuple(tpl[i:i + subtuple_size] for i in range(0, len(tpl), subtuple_size))

    # 21. Repeat Elements
    @staticmethod
    def repeat_elements(tpl, times):
        return tuple(x for x in tpl for _ in range(times))

    # 22. Create Range Tuple
    @staticmethod
    def create_range_tuple(start, end):
        return tuple(range(start, end + 1))

    # 23. Reverse Tuple
    @staticmethod
    def reverse_tuple(tpl):
        return tpl[::-1]

    # 24. Check Palindrome
    @staticmethod
    def check_palindrome(tpl):
        return tpl == tpl[::-1]

    # 25. Get Unique Elements
    @staticmethod
    def get_unique_elements(tpl):
        seen = set()
        return tuple(x for x in tpl if not (x in seen or seen.add(x)))
