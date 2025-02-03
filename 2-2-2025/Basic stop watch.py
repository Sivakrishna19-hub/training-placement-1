import time

input("Press Enter to start...")
start_time = time.time()

input("Press Enter to stop...")
end_time = time.time()

print(f"Elapsed time: {round(end_time - start_time, 2)} seconds")
