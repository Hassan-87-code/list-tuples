
ROWS = 4
COLUMNS = 5


def print_plan(plan):
    print("\nSeating plan (X = taken, O = available)")
    print("    " + " ".join(str(column) for column in range(1, COLUMNS + 1)))
    for row_number, row in enumerate(plan, start=1):
        print(f"{row_number:>2}  " + " ".join(row))


def main():
    plan = [["O" for _ in range(COLUMNS)] for _ in range(ROWS)]
    print_plan(plan)

    while True:
        answer = input("\nBook a seat? Enter row and column (or Q to quit): ").strip()
        if answer.casefold() == "q":
            break

        parts = answer.split()
        if len(parts) != 2:
            print("Enter a row and column, such as '2 4', or Q to quit.")
            continue

        try:
            row, column = (int(part) for part in parts)
        except ValueError:
            print("Row and column must be numbers.")
            continue

        if not (1 <= row <= ROWS and 1 <= column <= COLUMNS):
            print(f"Choose a row from 1 to {ROWS} and a column from 1 to {COLUMNS}.")
            continue
        if plan[row - 1][column - 1] == "X":
            print("That seat is already taken.")
            continue

        plan[row - 1][column - 1] = "X"
        print_plan(plan)

    print("Booking finished.")


if __name__ == "__main__":
    main()
