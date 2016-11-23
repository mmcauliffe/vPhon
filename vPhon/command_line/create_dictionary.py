


import sys
import re
import os
import argparse

from ..vPhon import process_word, process_textfile, create_dictionary, save_dictionary


def main():

    usage = 'python vPhon.py <input> -d, --dialect N|C|S'


    # Command line options foo
    parser = argparse.ArgumentParser(usage)
    parser.add_argument('path', type = str, help = 'File path')
    parser.add_argument('output_path', type = str, help = 'File to save output in')
    parser.add_argument('-g', '--glottal', action='store_true', help='prepend glottal stops to onsetless syllables')
    parser.add_argument('-6', '--pham', action='store_true', help='phonetize tones as 1-6')
    parser.add_argument('-8', '--cao', action='store_true', help='phonetize tones as 1-4 + 5, 5b, 6, 6b')
    parser.add_argument('-p', '--palatals', action='store_true', help='use word-final palatal velars in Northern dialects')
    parser.add_argument('-t', '--tokenize', action='store_true', help='preserve underscores or hyphens in tokenized inputs (e.g., anh_ta = anh1_ta1)')
    parser.add_argument('-d', '--dialect', action='store', type=str.lower, help='specify dialect region ([N]orthern, [C]entral, [S]outhern)')
    args = parser.parse_args()

    if not args.dialect:
        sys.exit('Please enter a valid dialect.')
    if args.dialect not in ['n', 'c', 's']:
        sys.exit('Please enter a valid dialect.')

    if os.path.exists(args.text[0]):
        text = process_textfile(args.text[0])
    else:
        sys.exit('Error: The file {} could not be found.'.format(args.text[0]))

    dictionary = create_dictionary(text, args.dialect, args.glottal, args.pham, args.cao, args.palatals, args.tokenize)

    save_dictionary(dictionary, args.output_path)



if __name__ == '__main__':
    main()