from morze import decode
import pytest


@pytest.mark.parametrize(
    "source_string, result",
    [
        ('... --- ...', 'SOS'),
        ('.-   .-   .-', 'A A A'),
        ('.... .. --..--   .-- --- .-. .-.. -..', 'HI, WORLD'),
        ('.---- ..---   -.-. -..', '12 CD'),
    ],
)
def test_decode(source_string, result):
    assert decode(source_string) == result


if __name__ == '__main__':
    test_decode('... --- ...', 'SOS')
    test_decode('.-   .-   .-', 'A A A')
    test_decode('.... .. --..--   .-- --- .-. .-.. -..', 'HI, WORLD')
    test_decode('.---- ..---   -.-. -..', '12 CD')
