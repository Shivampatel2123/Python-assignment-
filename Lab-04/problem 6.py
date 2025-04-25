hour = int(input("Enter an hour: "))
if hour == 0:
    print("12 Midnight")
elif hour == 12:
    print("12 Noon")
elif hour < 12:
    print(f"{hour} AM")
else:
    print(f"{hour - 12} PM")

        
