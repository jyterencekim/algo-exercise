SEPARATOR = '.'

class Codec:

    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        l = len(strs)
        result = [f"{l}{SEPARATOR}"]
        for s in strs:
            result.append(f"{len(s)}{SEPARATOR}{s}{SEPARATOR}")
        return ''.join(result)


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        first_separator_idx = s.index(SEPARATOR)
        l = int(s[:first_separator_idx])
        result = []

        idx = first_separator_idx
        for i in range(l):
            next_idx = s.index(SEPARATOR, idx + 1)
            sub_l = int(s[idx + 1:next_idx])
            result.append(s[next_idx + 1:next_idx + 1 + sub_l])
            idx = next_idx + 1 + sub_l
        
        return result
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))