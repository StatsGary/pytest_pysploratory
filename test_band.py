# Usage: 
#   run single test: 
#       pytest test_band.py::test_when_add_more_than_max_members -s
#   run all tests:
#       pytest


from bands.bander import Band
import pytest

# Create a fixture to persist the class instantiation
@pytest.fixture
def band():
    # All setup for the fixture
    return Band(max_member_size=6)

def test_can_bands(band):
    band.add_band_name('Foo Fighters')
    assert band.number_of_bands()  == 1

def test_when_band_added_to_list(band):
    band.add_band_name('Foo Fighters')
    assert 'Foo Fighters' in band.get_bands()

def test_can_add_band_member(band):
    band.add_members('Dave Grohl')
    band.add_members('Taylor Hawkins')
    band.add_members('Chris Shiflett')
    band.add_members('Pat Smear')
    band.add_members('Nate Mendal')
    band.add_members('Rami Jaffee')
    assert band.number_of_members() == 6

def test_when_member_added(band):
    band.add_members('Dave Grohl')
    band.add_members('Taylor Hawkins')
    band.add_members('Chris Shiflett')
    band.add_members('Pat Smear')
    band.add_members('Nate Mendal')
    band.add_members('Rami Jaffee')

    assert 'Dave Grohl' in band.get_members()
    assert 'Nate Mendal' in band.get_members()

def test_when_add_more_than_max_members(band):
    for _ in range(6):
        band.add_members('Dave Grohl')

    with pytest.raises(OverflowError):
        band.add_members('Dave Grohl')
