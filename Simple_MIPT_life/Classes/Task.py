class Small_task():
    def __init__(self, subject, task, week, number, done):
        self._subject = subject
        self._task = task
        self._week = week
        self._number = number
        self._done = done

    @property
    def subject(self):
        return self._subject

    @property
    def task(self):
        return self._task

    @property
    def week(self):
        return self._week

    @property
    def number(self):
        return self._number

    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, new_done):
        if new_done != self._done:
            self._done = new_done
        return self._done
