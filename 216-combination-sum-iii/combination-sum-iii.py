class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        """
        combination of k numbers summing up to n
        = some elt x + comb of (k - 1) summing to (n - x) if exists
        """
        answers = []
        def search(k_left: int, sum_left: int, i: int, acc: List[int]) -> None:
            if sum_left < 0:
                return
            if sum_left == 0:
                if k_left == 0:
                    answers.append(tuple(acc))
                return
            if i > 9:
                return
            
            acc.append(i)
            search(k_left - 1, sum_left - i, i + 1, acc)
            acc.pop()
            search(k_left, sum_left, i + 1, acc)
        
        search(k, n, 1, [])
        return answers
