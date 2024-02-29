import time

def timer(func):
    def wrapper():
        print("function started")
        start_time = time.time()
        result = func()
        end_time = time.time()
        print(f"Time taken to execute {func.__name__}: {end_time - start_time} seconds")
        print("function ended")
        return result
    return wrapper

# Example function to test the timer
def example_function():
    # Simulating some time-consuming task
    time.sleep(2)

# Using the timer function decorator
timed_example_function = timer(example_function)
timed_example_function()
