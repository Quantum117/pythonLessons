from collections import defaultdict

class DictionaryTasks:
    # 1. Get Value
    @staticmethod
    def get_value(dictionary, key, default=None):
        return dictionary.get(key, default)

    # 2. Check Key
    @staticmethod
    def check_key(dictionary, key):
        return key in dictionary

    # 3. Count Keys
    @staticmethod
    def count_keys(dictionary):
        return len(dictionary)

    # 4. Get All Keys
    @staticmethod
    def get_all_keys(dictionary):
        return list(dictionary.keys())

    # 5. Get All Values
    @staticmethod
    def get_all_values(dictionary):
        return list(dictionary.values())

    # 6. Merge Dictionaries
    @staticmethod
    def merge_dictionaries(dict1, dict2):
        merged_dict = dict1.copy()  # To avoid modifying the original dictionaries
        merged_dict.update(dict2)
        return merged_dict

    # 7. Remove Key
    @staticmethod
    def remove_key(dictionary, key):
        if key in dictionary:
            del dictionary[key]
        return dictionary

    # 8. Clear Dictionary
    @staticmethod
    def clear_dictionary(dictionary):
        dictionary.clear()
        return dictionary

    # 9. Check if Dictionary is Empty
    @staticmethod
    def check_empty(dictionary):
        return len(dictionary) == 0

    # 10. Get Key-Value Pair
    @staticmethod
    def get_key_value_pair(dictionary, key):
        if key in dictionary:
            return (key, dictionary[key])
        return None

    # 11. Update Value
    @staticmethod
    def update_value(dictionary, key, value):
        dictionary[key] = value
        return dictionary

    # 12. Count Value Occurrences
    @staticmethod
    def count_value_occurrences(dictionary, value):
        return list(dictionary.values()).count(value)

    # 13. Invert Dictionary
    @staticmethod
    def invert_dictionary(dictionary):
        return {v: k for k, v in dictionary.items()}

    # 14. Find Keys with Value
    @staticmethod
    def find_keys_with_value(dictionary, value):
        return [k for k, v in dictionary.items() if v == value]

    # 15. Create a Dictionary from Lists
    @staticmethod
    def create_dict_from_lists(keys, values):
        return dict(zip(keys, values))

    # 16. Check for Nested Dictionaries
    @staticmethod
    def check_for_nested_dictionaries(dictionary):
        return any(isinstance(v, dict) for v in dictionary.values())

    # 17. Get Nested Value
    @staticmethod
    def get_nested_value(dictionary, *keys):
        for key in keys:
            dictionary = dictionary.get(key, {})
        return dictionary

    # 18. Create Default Dictionary
    @staticmethod
    def create_default_dict(default_value):
        return defaultdict(lambda: default_value)

    # 19. Count Unique Values
    @staticmethod
    def count_unique_values(dictionary):
        return len(set(dictionary.values()))

    # 20. Sort Dictionary by Key
    @staticmethod
    def sort_dict_by_key(dictionary):
        return dict(sorted(dictionary.items()))

    # 21. Sort Dictionary by Value
    @staticmethod
    def sort_dict_by_value(dictionary):
        return dict(sorted(dictionary.items(), key=lambda item: item[1]))

    # 22. Filter by Value
    @staticmethod
    def filter_by_value(dictionary, condition):
        return {k: v for k, v in dictionary.items() if condition(v)}

    # 23. Check for Common Keys
    @staticmethod
    def check_common_keys(dict1, dict2):
        return bool(set(dict1.keys()) & set(dict2.keys()))

    # 24. Create Dictionary from Tuple
    @staticmethod
    def create_dict_from_tuple(tuple_of_pairs):
        return dict(tuple_of_pairs)

    # 25. Get the First Key-Value Pair
    @staticmethod
    def get_first_key_value_pair(dictionary):
        return next(iter(dictionary.items()), None)
