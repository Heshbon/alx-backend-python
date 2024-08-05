# Python_async_function

This project aims to deepen my understanding of asynchronous programming in Python, specifically using the `asyncio` library. The focus was on `async` and `await` syntax to manage concurrent coroutines effectively.

# Tasks 📃

# 0. The basics of async

  + <u>[0-basic_async_syntax.py]()</u>: Python asynchronous coroutine that takes in an integer argument (max_delay, with a default value of 10) named wait_random that waits for a random delay between 0 and max_delay.

# 1. Let's execute multiple coroutines at the same time with async

  + <u>[1-concurrent_coroutines.py]()</u>: Python async routine called wait_n that takes in 2 int arguments (in this order): n and max_delay.

#  2. Measure the runtime

  + <u>[2-measure_runtime.py]()</u>: Python async that import wait_n into 2-measure_runtime.py.

# 3. Tasks

  + <u>[3-tasks.py]()</u>: Python async that import wait_random from 0-basic_async_syntax.

#  4. Tasks

  + <u>[4-tasks.py]()</u>: Python file that defines the task_wait_n function, which performs a series of asynchronous waits with variable delays.
