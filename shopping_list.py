"""A small menu-driven shopping list."""


def main():
    items = []

    while True:
        print("\nShopping list")
        print("1. Add item")
        print("2. Remove item")
        print("3. View items")
        print("4. Sort items")
        print("5. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            item = input("Item to add: ").strip()
            if not item:
                print("Please enter an item.")
            elif any(existing.casefold() == item.casefold() for existing in items):
                print("That item is already on the list.")
            else:
                items.append(item)
                print(f"Added {item}.")
        elif choice == "2":
            item = input("Item to remove: ").strip()
            match = next(
                (existing for existing in items if existing.casefold() == item.casefold()),
                None,
            )
            if match is None:
                print("That item is not on the list.")
            else:
                items.remove(match)
                print(f"Removed {match}.")
        elif choice == "3":
            if items:
                for number, item in enumerate(items, start=1):
                    print(f"{number}. {item}")
            else:
                print("The list is empty.")
        elif choice == "4":
            items.sort(key=str.casefold)
            print("The list has been sorted.")
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
