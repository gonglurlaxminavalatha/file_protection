import base64

print("1. Protect file")
print("2. Restore file")

choice = input("Enter choice: ")

if choice == "1":
    text = input("Enter text: ")

    protected = base64.b64encode(text.encode()).decode()

    print("Protected text:", protected)

elif choice == "2":
    text = input("Enter protected text: ")

    restored = base64.b64decode(text.encode()).decode()

    print("Original text:", restored)

else:
    print("Invalid choice")
