"""Read ten marks and report basic statistics."""


def main():
    marks = []
    while len(marks) < 10:
        try:
            mark = float(input(f"Enter mark {len(marks) + 1} of 10: "))
        except ValueError:
            print("Please enter a number.")
            continue
        marks.append(mark)

    average = sum(marks) / len(marks)
    above_average = [mark for mark in marks if mark > average]

    print(f"Highest: {max(marks):g}")
    print(f"Lowest: {min(marks):g}")
    print(f"Average: {average:g}")
    print("Marks above average:", ", ".join(f"{mark:g}" for mark in above_average))
    print("Marks from highest to lowest:", ", ".join(f"{mark:g}" for mark in sorted(marks, reverse=True)))


if __name__ == "__main__":
    main()
