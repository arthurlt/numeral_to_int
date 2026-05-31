import argparse

from numeral_to_int.parser import parse as num_parser

def main() -> None:
	arg_parser = argparse.ArgumentParser(description="Convert Roman numerals to an integer")
	arg_parser.add_argument("numerals", type=str, help="Roman numerals you want converted")
	args = arg_parser.parse_args()
	
	print(num_parser(args.numerals))

if __name__ == "__main__":
	main()