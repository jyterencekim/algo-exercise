class Solution:
    def average(self, salary: List[int]) -> float:
        salary_max, salary_min = 0, math.inf
        salary_sum = 0
        for s in salary:
            salary_max = max(salary_max, s)
            salary_min = min(salary_min, s)
            salary_sum += s
        
        return (salary_sum - (salary_max + salary_min)) / (len(salary) - 2)