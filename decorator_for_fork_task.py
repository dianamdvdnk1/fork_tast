def worktime(f1, f2):
    def f(string):
        initial_time = time.time()
        f1(string)
        first = time.time() - initial_time
        initial_time = time.time()
        f2(string)
        second = time.time() - initial_time
        print(f1.name if first < second else f2.name)
    return f
    