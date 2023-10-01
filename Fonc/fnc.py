import argparse
from random import choice
from scanless.core import Scanless
import crayons

data = [
    ["Ipscan", "https://github.com/angryip/ipscan.git"],
    ["Advanced IP Scanner", "https://www.advanced-ip-scanner.com/"],
    ["IPinfo", "https://ipinfo.io/"]
]

version = "1.1"

sl = Scanless(cli_mode=True)

def parse_command_line_arguments():
    parser = argparse.ArgumentParser(
        description="Welcome to SecuNet..."
    )
    parser.add_argument(
        "-H",
        "--help_custom",
        action="store_true",
        help="Show options documentation..."
    )
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="Display version information..."
    )
    parser.add_argument(
        "-t",
        "--target",
        type=str,
        help="IP/PORT to scan..."
    )
    parser.add_argument(
        "-p",
        "--port",
        type=str,
        help="Target port..."
    )
    parser.add_argument(
        "-l",
        "--list",
        action="store_true",
        help="List scanners..."
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Output file name..."
    )
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="Use all the scanners..."
    )
    parser.add_argument(
        "-r",
        "--random",
        action="store_true",
        help="Use a random scanner..."
    )

    return parser

def display(results):
    for line in results.split("\n"):
        if not line:
            continue
        if "tcp" in line or "udp" in line:
            if "open" in line:
                line = crayons.green(line)
            if "closed" in line:
                line = crayons.red(line)
            if "filtered" in line:
                line = crayons.yellow(line)
        print(line)

def main():
    parser = parse_command_line_arguments()
    args = parser.parse_args()

    if args.version:
        print(f"v{version}")
        return

    if args.target and args.port:
        target = args.target
        port = args.port
        print(f"Scanning {target}:{port}...")
        # You can perform scanning or other operations here.
        return

    if args.output:
        with open(args.output, "w") as output_file:
            output_file.write("You can print this output to a file...\n")

    if args.list:
        for item in data:
            print(f"{item[0]}: {item[1]}")
        return

    if args.all:
        scanners = sl.scanners.keys()
        for scanner in scanners:
            print(f"{scanner}:")
            display(sl.scan(target, scanner=scanner)["raw"])
            print()

    if args.random:
        scanners = sl.scanners.keys()
        scanner = choice(list(scanners))
        print(f"{scanner}:")
        display(sl.scan(target, scanner=scanner)["raw"])

if __name__ == "__main__":
    main()