import webbrowser
import time

print("Generating codes...!")

filename = "list.txt"

with open(filename, 'r') as file:
    lines = file.readlines()
    i = 0
    for line in lines:
        try:
            webbrowser.open(line.strip())
            print(f"Generated coupon: {i + 1}")
            time.sleep(0.2)  # Sleep for 5 seconds
        except Exception as e:
            print(f"Error opening URL: {e}")

        i += 1
