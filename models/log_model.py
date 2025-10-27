class LogModel:
    def __init__(self):
        self.logs = []

    def store_log(self, log_entry):
        self.logs.append(log_entry)
        return True
