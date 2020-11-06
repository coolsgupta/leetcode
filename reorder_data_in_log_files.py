class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let_logs = []
        dig_logs = []

        for log in logs:
            iden, log_text = log.split(' ', maxsplit=1)
            if log_text[0].isalpha():
                # print(iden, log_text)
                let_logs.append((iden, log_text))
            else:
                dig_logs.append(log)

        return [' '.join(log) for log in sorted(let_logs, key=lambda x: (x[1], x[0]))] + dig_logs

