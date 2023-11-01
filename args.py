import sys


class Args:

    def __init__(self):
        self.year_start = None
        self.year_end = None

    def get_args(self):
        self.check_invalid_args()

    def check_invalid_args(self):
        arg_len = len(sys.argv)

        if arg_len != 6:
            print("Invalid number of arguments")
            exit(1)

        if not (sys.argv[1] == "gdp" and sys.argv[2] == "--from-year" and sys.argv[4] == "--to-year"):
            print("Invalid input in the form of \"gdp --from-year [year] --to-year [year]\"")
            exit(1)

        if not (sys.argv[3].isnumeric() and sys.argv[5].isnumeric()):
            print("Starting/Ending year must be a positive integer")
            exit(1)

        self.year_start = int(sys.argv[3])
        self.year_end = int(sys.argv[5])

        if not (999 < self.year_start < 10000 and 999 < self.year_end < 10000):
            print("Starting/Ending year must be a positive 4-digit integer")
            exit(1)

        if self.year_start > self.year_end:
            print("The starting year must be less than or equal to the ending year")
            exit(1)
