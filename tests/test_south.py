import pytest
import os
import sys

from vPhon.vPhon import process_word_dictionary

def test_basic(south_kwargs):
    assert(process_word_dictionary('cuỗm', delimiter = ' ', **south_kwargs) == ['k u_214 m'])
    #assert(process_word_dictionary('quen_biết', delimiter=' ', **south_kwargs) == ['w ɛ_33 ŋ b i_45 k'])
    assert(process_word_dictionary('ỏn_ẻn', delimiter=' ', **south_kwargs) == ['ɔ_214 ŋ ɛ_214 ŋ'])
