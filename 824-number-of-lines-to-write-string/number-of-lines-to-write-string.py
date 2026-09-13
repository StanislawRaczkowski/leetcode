class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        alphabet = list(map(chr, range(ord('a'), ord('z') + 1)))
        print(alphabet)
        lines = 1
        # last = 0
        pixels = 0
        for i in s:
            letter_width = widths[alphabet.index(i)]
            print(letter_width)
            if pixels + letter_width > 100:
                pixels = 0
                lines += 1
                last = 0
            pixels += letter_width
            # last += letter_width
        result = [lines, pixels]
        return result
            
            

            