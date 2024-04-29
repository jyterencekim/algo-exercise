class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        def get_opposite_party(s: chr) -> chr:
            if s == 'R':
                return 'D'
            return 'R'

        parties = {'R': "Radiant", 'D': "Dire"}
        canceled = Counter()
        freq = Counter(senate)
        q = deque()

        q.extend(senate)

        while len(q) > 1 and len(+freq) > 1:
            s = q.popleft()
            freq[s] -= 1
            if canceled[s] == 0:
                q.append(s)
                freq[s] += 1
                canceled[get_opposite_party(s)] += 1
            else:
                canceled[s] -= 1

        left = q[0]
        return parties[left]