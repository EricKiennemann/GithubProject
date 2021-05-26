import argparse
from plot import plot_analysis

def generate_analysis():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output",default='file', type=str, choices=['file','screen'],help="file or screen")
    args = parser.parse_args()
    print(f"output : {args.output}")
    plot_analysis(args.output)


if __name__ == "__main__":
   generate_analysis()
