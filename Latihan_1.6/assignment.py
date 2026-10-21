from not_yet_set_exception import NotYetSetException


class Assignment:
    def __init__(self):
        self.mark = -1

    def get_mark(self):
        if self.mark == -1:
            raise NotYetSetException("Mark is not yet set")
        return self.mark

    def set_mark(self, mark):
        self.mark = mark
