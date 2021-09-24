"""
Helper script to see how a string is tokenized by different tokenizers.

Usage:
    python scripts/tokenize_words.py -i [INPUT] -t [AUTO MODEL STRING]
"""
import argparse
import json
from statistics import mean
import transformers


def main(args):
    tokenizer = transformers.AutoTokenizer.from_pretrained(args.tokenizer)
    if args.input is not None:
        print(tokenizer.tokenize(args.input))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, default=None)
    parser.add_argument('-t', '--tokenizer', type=str, default='bert-base-uncased')
    args = parser.parse_args()

    main(args)

