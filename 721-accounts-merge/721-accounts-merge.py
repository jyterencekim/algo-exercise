import heapq
from collections import deque, defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        roots = dict()
        
        def find_root(email: str) -> str:
            if email not in roots:
                roots[email] = email
            if roots[email] != email:
                roots[email] = find_root(roots[email])
            return roots[email]
        
        def connect(x: str, y: str) -> str:
            xr, yr = find_root(x), find_root(y)
            roots[xr] = yr
            return xr
        
        def are_connected(x: str, y: str) -> bool:
            return find_root(x) == find_root(y)
        
        names_by_email = dict()
        
        for account in accounts:
            name, emails = account[0], account[1:]
            primary_email = emails[0]
            names_by_email[primary_email] = name
            for email in emails:
                connect(primary_email, email)
                
        mails_by_root = defaultdict(list)
        emails = roots.keys()
        
        for email in emails:
            mails_by_root[find_root(email)].append(email)
        
        def get_name(emails: List[str]) -> str:
            return [names_by_email[email] for email in emails if email in names_by_email][0]
        
        for root, mails in mails_by_root.items():
            name = get_name(mails)
            yield [name] + sorted(mails)
        
        
            