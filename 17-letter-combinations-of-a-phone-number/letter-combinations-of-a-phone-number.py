class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        Result = []
        FinRes = []
        templist = []
        lettuce = list(digits)
        LetComb = {2: ["a", "b", "c"], 3:['d', 'e', 'f'], 4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        for i in range(len(lettuce)):
            x = LetComb.get(int(lettuce[i]))
            for i in range(len(x)):
                for j in range(len(templist)):
                    FinRes.append(templist[j] + x[i])
            templist = FinRes + x       
        if FinRes == []:
            FinRes = templist
        if len(lettuce) == 3:
            for l in reversed(range(len(FinRes))):
                print(FinRes[l], len(FinRes[l]))
                if len(FinRes[l]) != 3:
                    FinRes.pop(l)
        if len(lettuce) == 4:
            for i in reversed(range(len(FinRes))):
                if len(FinRes[i]) != 4:
                    FinRes.pop(i)

        print(templist)

        return FinRes
