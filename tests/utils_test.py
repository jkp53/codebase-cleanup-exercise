from app.utils import to_usd

def test_to_usd():
    assert to_usd(0.455555) == "$0.46"
    assert to_usd(12345.67) == "$12,345.67"
