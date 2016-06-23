
import winsound
print("Enter Frequency")
print("Must be from 37 to 32,675")
freq = int(input ("> "))

print("Enter Duration: ")

duration = int(input ("> "))
duration = duration * 100
winsound.Beep(freq, duration)

