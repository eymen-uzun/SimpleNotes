import time

notlar = []

print("Hello user")
time.sleep(1)
print("This is basically a notes app")
time.sleep(1)
print("You can add notes and view them anytime")

while True:
    print("\nMenu:")
    print("1. Add a note")
    print("2. View notes")
    print("3. Exit")
    
    secim = input(": ")

    if secim == "1":
        yeni_not = input("Enter your note: ")
        notlar.append(yeni_not)
        print("Note added!")
    elif secim == "2":
        if notlar:
            print("Your notes:")
            for i, n in enumerate(notlar, start=1):
                print(f"{i}. {n}")
        else:
            print("No notes yet.")
    elif secim == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid selection, try again.")
