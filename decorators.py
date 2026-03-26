import time

#decorator to measure time
def measure_time(func):
    def wrapper(self, *args, **kwargs):
        start_time = time.time()
        result = func(self, *args, **kwargs)
        end_time = time.time()
        self.elapsed = end_time - start_time
        return result
    return wrapper