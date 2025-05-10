import sys
import time
import itertools
import threading


# loading function
def loading_message(message, duration=3):
    done_message = message + "done"
    animation    = itertools.cycle(['|', '/', '-', '\\'])
    
    start_time = time.time()
    while time.time() - start_time < duration:
        sys.stdout.write(f"\r{message}{next(animation)}")
        sys.stdout.flush()
        time.sleep(0.15)
    
    sys.stdout.write(f"\r{done_message}\n")
    sys.stdout.flush()


# thread function
def run_loading(message, duration=3):
    thread = threading.Thread(target=loading_message, args=(message, duration))
    thread.start()
    return thread  # return thread to join later if needed


# root
if __name__ == "__main__":
    # run multiple loading animations in sequence
    t1 = run_loading("Starting your program......", 5)
    t1.join()  # ensure first thread completes before moving to next

    t2 = run_loading("Complete program process......", 5)
    t2.join()

    input("All tasks completed. Press <enter> to continue")
