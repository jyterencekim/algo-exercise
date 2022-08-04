from enum import Enum

class LogType(Enum):
    LETTER = 0
    DIGIT = 1


class Log:
    def __init__(self, log):
        identifier, *logs = log.split()
        self.identifier = identifier
        self.log_type = LogType.LETTER if logs[0].isalpha() else LogType.DIGIT
        self.logs = " ".join(logs)
    def __str__(self):
        return " ".join([self.identifier, self.logs])
        
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        deserialized = [Log(log) for log in logs]
        
        letter_logs = list(filter(lambda log: log.log_type == LogType.LETTER, deserialized))
        digit_logs = list(filter(lambda log: log.log_type == LogType.DIGIT, deserialized))
        
        # assuming stable sort
        letter_logs.sort(key=lambda log: (log.logs, log.identifier))
        
        return [str(log) for log in letter_logs + digit_logs]
        