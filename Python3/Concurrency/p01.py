"""
Problem 1 of 10 — "Hello from a thread"
Write a function print_message(msg) that prints the given message. Then create two threads — one that prints "Hello from Thread 1" and one that prints "Hello from Thread 2". Start both threads and wait for both to finish before the main program exits.
"""
import threading

def print_message(msg):
    print(f'Hello from a thread {msg}')
    
def main1():
    t1 = threading.Thread(target=print_message, args=[1])
    t2 = threading.Thread(target=print_message, args=[2])
    
    t1.start()
    t2.start()
    
    t1.join()
    t2.join()