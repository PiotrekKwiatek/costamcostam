import time

def slow_function():
    print("Rozpoczynam działanie slow_function...")
    time.sleep(3) # tutaj program stoi przez 3 s
    print("Zakonczylem dzialanie slow_function")

print("Zaczynam pomiar czasu")
start_time = time.time() # znacznik czasu w momencie startu pomiaru

slow_function()

end_time = time.time() # znacznik czasu w momencie zakonczenia pomiaru 

elapsed_time = end_time - start_time # różnica czasu

print(f"Funkcja wykonała się w czasie {elapsed_time} sekund")

