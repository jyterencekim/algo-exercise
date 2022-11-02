class Solution:
    def maskPII(self, s: str) -> str:
        def mask_email(x: str) -> str:
            x = x.lower()
            pivot = x.find('@')
            name = x[:pivot]
            first, last = name[0], (name[-1] if len(name) > 1 else '')
            return first + '*****' + last + x[pivot:]
            
        
        def mask_number(x: int) -> str:
            return '*' * len(str(x))
        
        def regularize_phone(x: str) -> Tuple:
            groups = re.split(r'\W+', x)
            number = ''.join(groups)
            country_number = []
            local_number = number[-10:]
            local_numbers = [local_number[:3], local_number[3:6], local_number[6:]]
            
            if len(number) > 10:
                country_number = [number[:-10]]
            
            return [country_number, local_numbers]
        
        def mask_phone(x: str) -> str:
            country_num, local_nums = regularize_phone(x)
            c = '+' + mask_number(country_num[0]) if country_num else ''
            ll = [mask_number(n) for n in local_nums[:-1]] + [local_nums[-1]]
            
            if c:
                return '-'.join([c] + ll)
            return '-'.join(ll)
        
        if '@' in s:
            return mask_email(s)
        return mask_phone(s)