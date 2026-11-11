import threading
import time

# Create three distinct resources (representing the three corners of the triangle)
corner_a = threading.Lock()
corner_b = threading.Lock()
corner_c = threading.Lock()

def process_corner_1():
    """Rule 1: Lock Corner A, then try to connect to Corner B."""
    print("[Thread 1] Initializing Corner A (Valid local step)...")
    with corner_a:
        time.sleep(0.5)  # Pause to let other threads initialize their local steps
        print("[Thread 1] Reaching for Corner B...")
        with corner_b:
            print("[Thread 1] Connection successful! (This line will never print)")

def process_corner_2():
    """Rule 2: Lock Corner B, then try to connect to Corner C."""
    print("[Thread 2] Initializing Corner B (Valid local step)...")
    with corner_b:
        time.sleep(0.5)
        print("[Thread 2] Reaching for Corner C...")
        with corner_c:
            print("[Thread 2] Connection successful! (This line will never print)")

def process_corner_3():
    """Rule 3: Lock Corner C, then try to connect to Corner A."""
    print("[Thread 3] Initializing Corner C (Valid local step)...")
    with corner_c:
        time.sleep(0.5)
        print("[Thread 3] Reaching for Corner A...")
        with corner_a:
            print("[Thread 3] Connection successful! (This line will never print)")

# Run all three rules simultaneously
if __name__ == "__main__":
    print("--- Starting the Penrose Loop Simulation ---")
    
    t1 = threading.Thread(target=process_corner_1)
    t2 = threading.Thread(target=process_corner_2)
    t3 = threading.Thread(target=process_corner_3)
    
    t1.start()
    t2.start()
    t3.start()
    
    t1.join()
    t2.join()
    t3.join()
    
    print("--- Simulation Complete (This will never be reached) ---")