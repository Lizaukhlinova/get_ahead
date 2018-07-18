class FlattenedIterator():
    def __init__(self, *args):
        self.iters = args
        self.cur_index = -1
        self.iters_num = len(args)
        self.ended = []

    def __iter__(self):
        return self

    def __next__(self):
        try:
            self.cur_index = (self.cur_index + 1) % self.iters_num
            next_value = next(self.iters[self.cur_index])
        except StopIteration:
            self.ended.append(self.cur_index)
            if len(self.ended) == self.iters_num:
                raise StopIteration
            next_value = next(self)
        return next_value
