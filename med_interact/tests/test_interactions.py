import pytest
from med_interact.interactions import check_interaction

def test_check_interaction():
    result = check_interaction("Paracetamol", "Ibuprofeno")
    assert result["interaction_type"] == "moderate"
