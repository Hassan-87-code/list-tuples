"""Sort towns from north to south by latitude."""


def main():
    towns = [
        (51.5072, "London", -0.1276),
        (40.7128, "New York", -74.0060),
        (-33.8688, "Sydney", 151.2093),
        (35.6762, "Tokyo", 139.6503),
        (48.8566, "Paris", 2.3522),
    ]

    for latitude, name, longitude in sorted(towns, reverse=True):
        print(f"{name}: latitude {latitude}, longitude {longitude}")


if __name__ == "__main__":
    main()
