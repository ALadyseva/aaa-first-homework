from unittest.mock import patch
from what_is_year_now import what_is_year_now
import io
import unittest


class TestWhatYearIsNow(unittest.TestCase):
    def test_what_year_cases_1(self):
        dic = io.StringIO('{"$id": "1", "currentDateTime": "2023-11-05T20:24Z", "utcOffset": "00:00:00", "isDayLightSavingsTime": false, "dayOfTheWeek": "Sunday", "timeZoneName": "UTC","currentFileTime": 133436894845030700, "ordinalDate": "2023-309", "serviceResponse": null}')
        with patch("what_is_year_now.urllib.request.urlopen") as w_year_cases:
            w_year_cases.return_value = dic
            assert what_is_year_now() == 2023
            w_year_cases.assert_called_once()

    def test_what_year_cases_2(self):
        dic = io.StringIO('{"$id": "1", "currentDateTime": "05.11.2023T20:24Z", "utcOffset": "00:00:00", "isDayLightSavingsTime": false, "dayOfTheWeek": "Sunday", "timeZoneName": "UTC","currentFileTime": 133436894845030700, "ordinalDate": "2023-309", "serviceResponse": null}')
        with patch("what_is_year_now.urllib.request.urlopen") as w_year_cases:
            w_year_cases.return_value = dic
            assert what_is_year_now() == 2023
            w_year_cases.assert_called_once()

    def test_what_year_cases_3(self):
        dic = io.StringIO('{"$id": "1", "currentDateTime": "05/11/2023T20:24Z", "utcOffset": "00:00:00", "isDayLightSavingsTime": false, "dayOfTheWeek": "Sunday", "timeZoneName": "UTC","currentFileTime": 133436894845030700, "ordinalDate": "2023-309", "serviceResponse": null}')
        with patch("what_is_year_now.urllib.request.urlopen") as w_year_cases:
            w_year_cases.return_value = dic
            with self.assertRaises(ValueError):
                what_is_year_now()


if __name__ == '__main__':  # pragma: no cover
    testing = TestWhatYearIsNow()
    testing.test_what_year_cases_1
    testing.test_what_year_cases_2
    testing.test_what_year_cases_3
