import heapq
from collections import deque, defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        all_mails = set()
        connected = defaultdict(set) # (name, mail) -> (name, mail) connections
        
        for account in accounts:
            name, mails = account[0], account[1:]
            
            for i in range(len(mails)):
                mail = (name, mails[i])
                all_mails.add(mail)
                if i + 1 < len(mails):
                    next_mail = (name, mails[i + 1])
                    connected[mail].add(next_mail)
                    connected[next_mail].add(mail)
            
        visited = set()
        
        for mail in all_mails:
            if mail not in visited:
                q = deque()
                mails = set()
                q.append(mail)
                name = mail[0]
                
                while q:
                    account = q.popleft()
                    if account in visited:
                        continue
                    visited.add(account)
                    mails.add(account[1])
                    
                    for related in connected[account]:
                        q.append(related)
                
                yield [name, *sorted(mails)]
                