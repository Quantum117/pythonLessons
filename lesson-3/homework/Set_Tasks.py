import random

class SetTasks:
    # 1. Union of Sets
    @staticmethod
    def union_of_sets(set1, set2):
        return set1 | set2

    # 2. Intersection of Sets
    @staticmethod
    def intersection_of_sets(set1, set2):
        return set1 & set2

    # 3. Difference of Sets
    @staticmethod
    def difference_of_sets(set1, set2):
        return set1 - set2

    # 4. Check Subset
    @staticmethod
    def check_subset(set1, set2):
        return set1.issubset(set2)

    # 5. Check Element
    @staticmethod
    def check_element(s, element):
        return element in s

    # 6. Set Length
    @staticmethod
    def set_length(s):
        return len(s)

    # 7. Convert List to Set
    @staticmethod
    def convert_list_to_set(lst):
        return set(lst)

    # 8. Remove Element
    @staticmethod
    def remove_element(s, element):
        s.discard(element)  # discard doesn't raise an error if element is not present
        return s

    # 9. Clear Set
    @staticmethod
    def clear_set(s):
        s.clear()
        return s

    # 10. Check if Set is Empty
    @staticmethod
    def check_empty_set(s):
        return len(s) == 0

    # 11. Symmetric Difference
    @staticmethod
    def symmetric_difference(set1, set2):
        return set1 ^ set2

    # 12. Add Element
    @staticmethod
    def add_element(s, element):
        s.add(element)
        return s

    # 13. Pop Element
    @staticmethod
    def pop_element(s):
        return s.pop() if s else None

    # 14. Find Maximum
    @staticmethod
    def find_maximum(s):
        return max(s) if s else None

    # 15. Find Minimum
    @staticmethod
    def find_minimum(s):
        return min(s) if s else None

    # 16. Filter Even Numbers
    @staticmethod
    def filter_even_numbers(s):
        return {x for x in s if x % 2 == 0}

    # 17. Filter Odd Numbers
    @staticmethod
    def filter_odd_numbers(s):
        return {x for x in s if x % 2 != 0}

    # 18. Create a Set of a Range
    @staticmethod
    def create_set_of_range(start, end):
        return set(range(start, end + 1))

    # 19. Merge and Deduplicate
    @staticmethod
    def merge_and_deduplicate(lst1, lst2):
        return set(lst1 + lst2)

    # 20. Check Disjoint Sets
    @staticmethod
    def check_disjoint_sets(set1, set2):
        return set1.isdisjoint(set2)

    # 21. Remove Duplicates from a List
    @staticmethod
    def remove_duplicates_from_list(lst):
        return list(set(lst))

    # 22. Count Unique Elements
    @staticmethod
    def count_unique_elements(lst):
        return len(set(lst))

    # 23. Generate Random Set
    @staticmethod
    def generate_random_set(size, start, end):
        return {random.randint(start, end) for _ in range(size)}
