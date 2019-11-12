import pytest
import sys, os
# This block is not neccessary if you instaled your package
# using e.g. pip install -e
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__), # location of this file
            os.pardir, # and one level up, in linux ../
        )
    )
)
# EOBlock

import playground

def test_black_spots():
    peaks = playground.colortest.find_black_spots([(255,255,255), (0,0,0), (255,255,255)])
    assert peaks == [1]
    
def test_two_black_spots():
    peaks = playground.colortest.find_black_spots([(255,255,255), (0,0,0), (255,255,255), (0,0,0), (255,255,255)])
    assert peaks == [1, 3]
    
def test_black_spots_corner_case():
    peaks = playground.colortest.find_black_spots([(0,0,0), (255,255,255), (255,255,255)])
    assert peaks == []
    
def test_black_spots_empty_list():
    peaks = playground.colortest.find_black_spots([])
    assert peaks == []
