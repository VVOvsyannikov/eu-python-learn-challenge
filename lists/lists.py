class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        if not input_list:
            return input_list

        max_number = input_list[0]

        for n in input_list:
            if n > max_number:
                max_number = n

        for i, value in enumerate(input_list):
            if value > 0:
                input_list[i] = max_number

        return input_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        if not input_list:
            return -1

        def recursion(left: int, right: int) -> int:
            if left > right:
                return -1

            mid = (left + right) // 2
            value = input_list[mid]

            if value == query:
                return mid
            elif value > query:
                return recursion(left, mid - 1)
            else:
                return recursion(mid + 1, right)

        return recursion(0, len(input_list) - 1)
