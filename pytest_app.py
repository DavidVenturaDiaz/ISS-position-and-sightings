from app.py import read_data_from_file_into_dict
from app.py import interaction_info
from app.py import print_epochs
import pytest

def test_read_data_from_file_into_dict():
    assert read_data_from_file_into_dict() == 'Data has been read from file'

def test_interaction_info():
    assert isinstance(interaction_info(), str) == True

def test_print_epochs():
    assert isinstance(print_epochs(), str) == True
