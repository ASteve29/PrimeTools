import sys
import prime_utils as pr

def list_commands():
    print("Available commands:")
    print("  check <n>   - check if a number is prime")
    print("  next <n>    - finds the next prime after a number")
    print("  prev <n>    - finds the previous prime before a number")
    print("  gen <n>     - generates primes upto a number")
    print("  count <n>   - counts the amount if primes under a number")
    print("  fac <n>     - lists the prime factors of a number")
    print("  help        - list available commands")

def handle_command(command, value):
    match command:
        case "check":
            print(f"{value} is prime!" if pr.is_prime(value) else f"{value} isn't prime!")
        case "next":
            print(f"The next prime after {value} is {pr.next_prime(value)}")
        case "prev":
            print(f"The previous prime before {value} is {pr.previous_prime(value)}")
        case "gen":
            print(f"The primes up to {value} are {pr.generate_primes_up_to(value)}")
        case "count":
            print(f"The number of primes below {value} is {pr.count_primes_up_to(value)}")
        case "fac":
            print(f"The factors of {value} are {pr.factor(value)}")
        case _:
            print("Unknown command.")
            list_commands()


def main():
    if len(sys.argv) < 2:
        list_commands()
        return

    command = sys.argv[1]

    if command == "help":
        list_commands()
        return

    if len(sys.argv) < 3:
        list_commands()
        print("Usage: python main.py <function> <number>")
        return

    try:
        value = int(sys.argv[2])
    except ValueError:
        print("Error: the second argument must be a number")
        return

    handle_command(command, value)

if __name__ == "__main__":
    main()
