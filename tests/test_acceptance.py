import pytest

from moviematch.api import NoHistoryError, recommend


def test_rated_user_gets_affinity_ranked_movies():
    assert recommend("u-ana") == ["m07", "m06", "m05"]


def test_rated_titles_are_not_recommended_again():
    assert not {"m01", "m04", "m02"} & set(recommend("u-ana", limit=8))


def test_genre_filter():
    assert recommend("u-ben", genre="family") == ["m05"]


def test_limit_is_respected():
    assert len(recommend("u-ben", limit=2)) == 2


def test_unknown_user_has_no_history():
    with pytest.raises(NoHistoryError):
        recommend("u-new")
