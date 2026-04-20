from demo_app.calculator import add, is_even


def main() -> None:
    total = add(20, 22)
    parity = "even" if is_even(total) else "odd"
    print(f"Result: {total} ({parity})")


if __name__ == "__main__":
    main()
