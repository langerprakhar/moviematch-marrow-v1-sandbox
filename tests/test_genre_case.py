import pytest

from moviematch.api import recommend


@pytest.mark.parametrize("genre", ["family", "Family", "FAMILY", "fAmIlY"])
def test_genre_filter_ignores_case(genre):
    assert recommend("u-ben", genre=genre) == ["m05"]


def test_mixed_case_genre_matches_lowercase_result():
    assert recommend("u-ana", limit=8, genre="SciFi") == ["m07"]
    assert recommend("u-ana", limit=8, genre="SciFi") == recommend("u-ana", limit=8, genre="scifi")


def test_no_genre_is_unaffected():
    assert recommend("u-ana") == ["m07", "m06", "m05"]
