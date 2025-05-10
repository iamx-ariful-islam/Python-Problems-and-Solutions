import time
import logging
import threading


def thread_function(name):
  print("Thread %s: starting" % name)
  # logging.info("Thread %s: starting", name)
  time.sleep(3)
  print("Thread %s: finishing" % name)
  # logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
  # format = "%(asctime)s: %(message)s"
  # logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

  threads = list()
  for index in range(3):
    
    print("Main    : create and start thread %d." % index)
    # logging.info("Main    : create and start thread %d.", index)
    x = threading.Thread(target=thread_function, args=(index,))
    threads.append(x)
    x.start()

  for index, thread in enumerate(threads):
    print("Main    : before joining thread %d." % index)
    # logging.info("Main    : before joining thread %d.", index)
    thread.join()
    print("Main    : thread %d done" % index)
    # logging.info("Main    : thread %d done", index)