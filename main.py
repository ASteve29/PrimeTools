import sys
import prime_wrapper as pr

def list_commands():
    print("Available commands:")
    print("  isprime <n>   - check if a number is prime")
    print("  nextprime <n>    - finds the next prime after a number")
    print("  prevprime <n>    - finds the previous prime before a number")
    print("  genprimes <n>     - generates primes upto a number")
    print("  countprimes <n>   - counts the amount if primes under a number")
    print("  factor <n>     - lists the prime factors of a number")
    print("  help        - list available commands")

def handle_command(command, value):
    match command:
        case "isprime":
            print(f"{value} is prime!" if pr.py_is_prime(value) else f"{value} isn't prime!")
        case "nextprime":
            print(f"The next prime after {value} is {pr.py_next_prime(value)}")
        case "prevprime":
            print(f"The previous prime before {value} is {pr.py_previous_prime(value)}")
        case "genprimes":
            print(f"The primes up to {value} are {pr.py_generate_primes_up_to(value)}")
        case "countprimes":
            print(f"The number of primes below {value} is {pr.py_count_primes_up_to(value)}")
        case "factor":
            print(f"The factors of {value} are {pr.py_factor(value)}")
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
