def mul2(x):
    return x % 2 == 0

def mul3(x):
    return x % 3 == 0

def mul5(x):
    return x % 5 == 0


class multifilter:
    def compare(self):
        positive_values_count = 0
        for function in self.funcs:
            function_value = function(self.iterable[self.index - 1])
            if function_value:
                positive_values_count += 1
        return positive_values_count

    def judge_any(self):
        count_of_positive = self.compare()
        if count_of_positive >= 1:
            return True
        else:
            return False

    def judge_half(self):
        count_of_functions = len(self.funcs)
        count_of_positive = self.compare()
        if count_of_positive >= count_of_functions / 2:
            return True
        else:
            return False

    def judge_all(self):
        count_of_functions = len(self.funcs)
        count_of_positive = self.compare()
        if count_of_positive == count_of_functions:
            return True
        else:
            return False

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.judge = judge
        self.index = 0
        self.funcs = funcs

    def __next__(self):
        while True:
            if self.index >= len(self.iterable):
                raise StopIteration
            self.index += 1
            current_value = self.iterable[self.index - 1]
            decide_bool_value = self.judge(self)
            if decide_bool_value:
                return current_value
            elif self.index >= len(self.iterable):
                raise StopIteration


    def __iter__(self):
        return self


a = [i for i in range(31)] # [0, 1, 2, ... , 30]

print(list(multifilter(a, mul2, mul3, mul5)))
# [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# [0, 6, 10, 12, 15, 18, 20, 24, 30]

print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# [0, 30]