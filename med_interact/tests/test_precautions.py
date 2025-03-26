import pytest
from med_interact.precautions import get_precautions

def test_get_precautions():
    precautions = get_precautions("Warfarin", "Aspirina")
    assert "Evite o uso com álcool" in precautions
