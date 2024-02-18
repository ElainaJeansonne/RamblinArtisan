import sys, time, os

message = 'Hello World!'

for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)

def print_rgb(text, r, g, b):
    color_code = f"\033[38;2;{r};{g};{b}m"
    print(f"{color_code}{text}\033[0m")

print_rgb(message, 255, 0, 0)