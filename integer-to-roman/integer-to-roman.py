class Solution:
    def intToRoman(self, num: int) -> str:
        romans = "MDCLXVI"
        nums = [1000, 500, 100, 50, 10, 5, 1]
        ones = {1000, 100, 10}
        fives = {500, 50, 5}
        roman_to_num = {roman: nums[i] for i, roman in enumerate(romans)}
        num_to_roman = {num: romans[i] for i, num in enumerate(nums)}
        
        result = ""
        carry = num
        order = 0 # unit index from nums
        while carry:
            unit = nums[order]
            
            quotient = carry // unit
            remainder = carry % unit
            
            result += quotient * num_to_roman[unit]
            carry -= quotient * unit
            
            # Handle 9
            if unit in ones:
                unit_lesser = unit // 10
                if remainder // unit_lesser == 9:
                    # the remainder must be expressed by quotient * this + lesser + this
                    result += num_to_roman[unit_lesser] + num_to_roman[unit]
                    carry -= 9 * unit_lesser 
            # Handle 4
            elif unit in fives:
                unit_lesser = nums[order + 1]
                if remainder // unit_lesser == 4:
                    result += num_to_roman[unit_lesser] + num_to_roman[unit]
                    carry -= unit + 4 * unit_lesser
            order += 1
        
        return result
            
            
            