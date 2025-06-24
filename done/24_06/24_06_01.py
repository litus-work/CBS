from typing import List

def int_list_to_str_list(numbers: List[int]) -> List[str]:
    return [str(num) for num in numbers]

input_list = [1, 2, 3, 42, 100]
# result = int_list_to_str_list(['a', 'b', 'c'])
result = int_list_to_str_list(input_list)

print("Список рядків:", result)