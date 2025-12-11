class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        if not input_list:
            return input_list

        max_number = max(input_list)

        for i, value in enumerate(input_list):
            if value > 0:
                input_list[i] = max_number

        return input_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        if not input_list:
            return -1

        left, right = 0, len(input_list) - 1

        while left <= right:
            mid = (left + right) // 2
            value = input_list[mid]

            if value == query:
                return mid
            elif value > query:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    @staticmethod
    def search_with_recursion(input_list: list[int], query: int) -> int:
        if not input_list:
            return -1

        def recursion_search(left: int, right: int) -> int:
            if left > right:
                return -1

            mid = (left + right) // 2
            value = input_list[mid]

            if value == query:
                return mid
            elif value > query:
                return recursion_search(left, mid - 1)
            else:
                return recursion_search(mid + 1, right)

        return recursion_search(0, len(input_list) - 1)
