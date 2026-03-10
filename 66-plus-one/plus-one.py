class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        List = "".join(str(i) for i in digits)
        New = int(List) + 1
        Final = [int(i) for i in str(New)]

        print(List)
        print(New)
        return Final