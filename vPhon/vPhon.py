#coding: utf-8

###########################################################################
#       vPhon.py version 0.2.5b
#       Copyright 2008-2016 James Kirby <j.kirby@ed.ac.uk>
#
#
#       vPhon is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       vPhon is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with vPhon.  If not, see <http://www.gnu.org/licenses/>.
#
###########################################################################

import sys
import re
import os
import argparse
from string import punctuation
import itertools


def trans(word, dialect, glottal, pham, cao, palatals):

    # This looks ugly, but newer versions of python complain about "from x import *" syntax
    if dialect == 'n':
        from .Rules.north import onsets, nuclei, codas, tones, onglides, offglides, onoffglides, qu, gi
    elif dialect == 'c':
        from .Rules.central import onsets, nuclei, codas, tones, onglides, offglides, onoffglides, qu, gi
    elif dialect == 's':
        from .Rules.south import onsets, nuclei, codas, tones, onglides, offglides, onoffglides, qu, gi

    if pham or cao:
        if dialect == 'n': from .Rules.north import tones_p
        if dialect == 'c': from .Rules.central import tones_p
        if dialect == 's': from .Rules.south import tones_p
        tones = tones_p

    ons = ''
    nuc = ''
    cod = ''
    ton = 0
    oOffset = 0
    cOffset = 0
    l = len(word)

    if l > 0:
        if word[0:3] in onsets:         # if onset is 'ngh'
            ons = onsets[word[0:3]]
            oOffset = 3
        elif word[0:2] in onsets:       # if onset is 'nh', 'gh', 'kʷ' etc
            ons = onsets[word[0:2]]
            oOffset = 2
        elif word[0] in onsets:         # if single onset
            ons = onsets[word[0]]
            oOffset = 1

        if word[l-2:l] in codas:        # if two-character coda
            cod = codas[word[l-2:l]]
            cOffset = 2
        elif word[l-1] in codas:        # if one-character coda
            cod = codas[word[l-1]]
            cOffset = 1


        #if word[0:2] == 'gi' and cod and len(word) == 3:  # if you just have 'gi' and a coda...
        if word[0:2] in gi and cod and len(word) == 3:  # if you just have 'gi' and a coda...
            nucl = 'i'
            ons = 'z'
        else:
            nucl = word[oOffset:l-cOffset]

        if nucl in nuclei:
            if oOffset == 0:
                if glottal == 1:
                    if word[0] not in onsets:   # if there isn't an onset....
                        ons = 'ʔ'+nuclei[nucl] # add a glottal stop
                    else:                       # otherwise...
                        nuc = nuclei[nucl]      # there's your nucleus
                else:
                    nuc = nuclei[nucl]          # there's your nucleus
            else:                               # otherwise...
                nuc = nuclei[nucl]              # there's your nucleus

        elif nucl in onglides and ons != 'kw': # if there is an onglide...
            nuc = onglides[nucl]                # modify the nuc accordingly
            if ons:                             # if there is an onset...
                if isinstance(ons, list):
                    ons = [x+'w' for x in ons]
                else:
                    ons = ons+'w'                  # labialize it, but...
            else:                               # if there is no onset...
                ons = 'w'                      # add a labiovelar onset

        elif nucl in onglides and ons == 'kw':
            nuc = onglides[nucl]

        elif nucl in onoffglides:
            cod = onoffglides[nucl][-1]
            nuc = onoffglides[nucl][0:-1]
            if ons != 'kw':
                if ons:
                    ons = ons+'w'
                else:
                    ons = 'w'
        elif nucl in offglides:
            cod = offglides[nucl][-1]
            nuc = offglides[nucl][:-1]

        else:
            # Something is non-Viet
            return (None, None, None, None)

        if word in gi:          # if word == 'gi'
            ons = gi[word][0]
            nuc = gi[word][1]

        if word in qu:          # if word == 'quy'
            ons = qu[word][:-1]
            nuc = qu[word][-1]


        # Velar Fronting (Northern dialect)
        if dialect == 'n':
            if nuc == 'a':
                if cod == 'k' and cOffset == 2: nuc = 'ɛ'
                if cod == 'ɲ' and nuc == 'a': nuc = 'ɛ'

            # Final palatals (Northern dialect)
            if nuc not in ['i', 'e', 'ɛ']:
                if cod == 'ɲ': cod = 'ŋ'
            elif palatals != 1 and nuc in ['i', 'e', 'ɛ']:
                if cod == 'ɲ': cod = 'ŋ'
            if palatals == 1:
                if cod == 'k' and nuc in ['i', 'e', 'ɛ']: cod = 'c'

        # Velar Fronting (Southern and Central dialects)
        else:
            if nuc in ['i', 'e']:
                if cod == 'k': cod = 't'
                if cod == 'ŋ': cod = 'n'

            # There is also this reverse fronting, see Thompson 1965:94 ff.
            elif nuc in ['iə', 'ɯə', 'uə', 'u', 'ɯ', 'ɤ', 'o', 'ɔ', 'ă', 'ɤ̆']:
                if cod == 't':
                    cod = 'k'
                if cod == 'n': cod = 'ŋ'

        # Monophthongization (Southern dialects: Thompson 1965: 86; Hoàng 1985: 181; MB - More than just labials)
        if dialect == 's':
            if cod in ['m', 'p', 'n', 't', 'ŋ', 'k', 'j', 'w']:
                if nuc == 'iə': nuc = 'iː'
                if nuc == 'uə': nuc = 'uː'
                if nuc == 'ɯə': nuc = 'ɯː'

        # Front vowel centralization before coronals - MB
        if dialect == 's':
            if cod in ['n', 't']:
                if nuc == 'i': nuc = 'ɯ'
                if nuc == 'e': nuc = 'ɤ'

        # Tones
        # Modified 20 Sep 2008 to fix aberrant 33 error
        tonelist = [tones[word[i]] for i in range(0,l) if word[i] in tones]
        if tonelist:
            ton = str(tonelist[len(tonelist)-1])
        else:
            if not (pham or cao):
                if dialect == 'c':
                    ton = '35'
                else:
                    ton = '33'
            else:
                ton = '1'

        # Modifications for closed syllables
        if cOffset !=0:

            # Obstruent-final nang tones are modal voice
            if (dialect == 'n' or dialect == 's') and ton == '21\u02C0' and cod in ['p', 't', 'k']:
                ton = '21'

            # Modification for sắc in closed syllables (Nothern and Central only)
            if (dialect == 'n' and ton == '24') or (dialect == 'c' and ton == '13'):
                ton = '45'

            # Modification for 8-tone system
            if cao == 1:
                if ton == '5' and cod in ['p', 't', 'k']:
                    ton = '5b'
                if ton == '6' and cod in ['p', 't', 'k']:
                    ton = '6b'

            # labialized allophony (added 17.09.08)
            labializing_vowels = ['u','o'] # Addressing a comment by Marc Brunelle, removed open o for southern - MM
            if dialect != 's':
                labializing_vowels += ['ɔ']
            if nuc in labializing_vowels:
                if cod == 'ŋ':
                    cod = 'ŋ͡m'
                if cod == 'k':
                    cod = 'k͡p'

        return [ons, nuc, ton, cod]

def convert_dictionary(word, dialect, glottal, pham, cao, palatals,delimiter = ''):
    """Convert a single orthographic string to IPA."""

    parts = list(trans(word, dialect, glottal, pham, cao, palatals))
    if parts is None or None in parts:
        return None
    if any(isinstance(x, list) for x in parts):
        for i,p in enumerate(parts):
            if not isinstance(p, list):
                parts[i] = [p]
        seqs = []
        for p in itertools.product(*parts):
            ons, nuc, ton, cod = p
            transcription = delimiter.join([ons, '_'.join([nuc, ton]), cod])
            seqs.append(transcription.strip())
    else:
        ons, nuc, ton, cod = parts
        transcription = delimiter.join([ons, '_'.join([nuc, ton]), cod])
        seqs = [transcription.strip()]

    return seqs

def process_word_dictionary(word, dialect, glottal, pham, cao, palatals, delimiter = ''):
    word = word.strip(punctuation).lower()
    ## 29.03.16: check if tokenize is true
    ## if true, call this routine for each substring
    ## and re-concatenate
    if '-' in word or '_' in word:
        substrings = re.split(r'(_|-)', word)
        values = substrings[::2]
        delimiters = substrings[1::2] + ['']

        ipa = [convert_dictionary(x, dialect, glottal, pham, cao, palatals, delimiter) for x in values]
        if None in ipa:
            return None
        seq = []
        for p in itertools.product(*ipa):
            seq.append(delimiter.join(p))
    else:
        seq = convert_dictionary(word, dialect, glottal, pham, cao, palatals, delimiter)
        if 'v' in word:
            print(word, seq)
    return seq

def convert(word, dialect, glottal, pham, cao, palatals,delimiter = ''):
    """Convert a single orthographic string to IPA."""

    parts = trans(word, dialect, glottal, pham, cao, palatals)
    if parts is None or None in parts:
        return ['['+word+']']
    if any(isinstance(x, list) for x in parts):
        for i,p in enumerate(parts):
            if not isinstance(p, list):
                parts[i] = [p]
        seqs = []
        for p in itertools.product(*parts):
            seqs.append(delimiter.join(p).strip())
    else:
        seqs = [delimiter.join(parts).strip()]

    return seqs

def process_word(word, dialect, glottal, pham, cao, palatals, tokenize, delimiter = ''):
    word = word.strip(punctuation).lower()
    ## 29.03.16: check if tokenize is true
    ## if true, call this routine for each substring
    ## and re-concatenate
    if (tokenize and '-' in word) or (tokenize and '_' in word):
        substrings = re.split(r'(_|-)', word)
        values = substrings[::2]
        delimiters = substrings[1::2] + ['']
        ipa = [convert(x, dialect, glottal, pham, cao, palatals, delimiter) for x in values]
        seq = ''.join(v + d for v, d in zip(ipa, delimiters))
    else:
        seq = ''.join(convert(word, dialect, glottal, pham, cao, palatals, delimiter))
    return seq


def process_textfile(path):
    with open(path, 'r', encoding='utf-8') as fh:
        text = []
        for line in fh:
            line = line.strip()
            line = line.split()
            line = [x for x in line if x not in ['', '_', '-']]
            if line:
                text.append(line)
    return text

def get_unique_words(text):
    words = set()
    for line in text:
        words.update(line)
    return sorted(words)

def create_dictionary(text, dialect, glottal, pham, cao, palatals, tokenize):
    words = get_unique_words(text)
    dictionary = {}
    for word in words:
        phones = process_word_dictionary(word, dialect, glottal, pham, cao, palatals, ' ')
        if phones is None:
            continue
        if word not in dictionary:
            dictionary[word] = []
        dictionary[word].extend(phones)
    return dictionary

def save_dictionary(dictionary, output_path):
    with open(output_path, 'w', encoding='utf8') as f:
        for k,v in sorted(dictionary.items()):
            if 'v' in k:
                print(k,v)
            for phones in v:
                f.write('{} {}\n'.format(k, phones))

def main():
    #sys.path.append('./Rules')      # make sure we can find the Rules files
    #sys.path.append('/Users/jkirby/Documents/Projects/vphon/Rules')

    usage = 'python vPhon.py <input> -d, --dialect N|C|S'


    # Command line options foo
    parser = argparse.ArgumentParser(usage)
    parser.add_argument('text', nargs='+', type = str, help = 'Text to convert or a file path')
    parser.add_argument('-g', '--glottal', action='store_true', help='prepend glottal stops to onsetless syllables')
    parser.add_argument('-6', '--pham', action='store_true', help='phonetize tones as 1-6')
    parser.add_argument('-8', '--cao', action='store_true', help='phonetize tones as 1-4 + 5, 5b, 6, 6b')
    parser.add_argument('-p', '--palatals', action='store_true', help='use word-final palatal velars in Northern dialects')
    parser.add_argument('-t', '--tokenize', action='store_true', help='preserve underscores or hyphens in tokenized inputs (e.g., anh_ta = anh1_ta1)')
    parser.add_argument('-d', '--dialect', action='store', type=str.lower, help='specify dialect region ([N]orthern, [C]entral, [S]outhern)')
    parser.add_argument('-o','--output_path', type = str, help = 'File to save output in')
    args = parser.parse_args()

    if not args.dialect:
        sys.exit('Please enter a valid dialect.')
    if args.dialect not in ['n', 'c', 's']:
        sys.exit('Please enter a valid dialect.')

    if os.path.exists(args.text[0]):
        text = process_textfile(args.text[0])
    else:
        if r'/' in args.text[0] or r'\\' in args.text[0]:
            sys.exit('Error: The file {} could not be found.'.format(args.text[0]))
        text = [args.text]

    # Now, parse the input
    converted = []
    for line in text:
        ortho = ' '.join(line)
        phones = ' '.join(process_word(x, args.dialect, args.glottal, args.pham, args.cao, args.palatals, args.tokenize) for x in line)
        converted.append(phones)
    if args.output_path:
        with open(args.output_path, 'w', encoding = 'utf8') as f:
            for line in converted:
                f.write(line)
                f.write('\n')


if __name__ == '__main__':
    main()
