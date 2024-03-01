import time
import unittest
from io import StringIO
from unittest.mock import patch


def timer(func):
    def wrapper(*args, **kwargs):
        print("function started")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken to execute {func.__name__}: {end_time - start_time} seconds")
        print("function ended")
        return result

    return wrapper


# Example function to test the timer
def example_function():
    # Simulating some time-consuming task
    time.sleep(2)


def example_function(duration):
    # Simulating some time-consuming task
    time.sleep(duration)


# Using the timer function decorator
timed_example_function = timer(example_function)
timed_example_function()


class TestTimerDecorator(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_timer_decorator(self, mock_stdout):
        with patch('time.sleep') as mock_sleep:
            timed_example_function("Test message", delay=1)
            output = mock_stdout.getvalue().strip()
            self.assertIn("Time taken to execute example_function", output)
            mock_sleep.assert_called_once_with(1)


if __name__ == '__main__':
    unittest.main()
