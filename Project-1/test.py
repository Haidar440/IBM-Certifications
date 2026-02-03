import time

FREQUENCY_PER_MINUTE = 60 # Number of iterations per minute

for i in range(5):
    print(f"Iteration {i + 1}")
    time.sleep(60 / FREQUENCY_PER_MINUTE) # Sleep to maintain the frequency of 45 iterations per minute where 60 seconds in a minute and FREQUENCY_PER_MINUTE is 45

