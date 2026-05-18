import argparse
import sys

def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--physics", type=int, required=True)
    parser.add_argument("--chemistry", type=int, required=True)
    parser.add_argument("--maths", type=int, required=True)
    args = parser.parse_args()
    avg = (args.physics + args.chemistry + args.maths) / 3
    print("Average marks:", avg)

if __name__ == "__main__":
    main(sys.argv[1:])