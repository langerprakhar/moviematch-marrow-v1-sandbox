import pytest

from moviematch.api import NoHistoryError, RATINGS, top_genres


@pytest.mark.parametrize(
    ("user_id", "expected"),
    [
        ("u-ana", ["scifi", "drama", "thriller"]),
        ("u-ben", ["comedy", "family"]),
    ],
)
def test_top_genres_orders_by_descending_affinity(user_id, expected):
    assert top_genres(user_id) == expected


def test_top_genres_unknown_user_has_no_history():
    with pytest.raises(NoHistoryError):
        top_genres("u-new")


def test_top_genres_empty_history(monkeypatch):
    monkeypatch.setitem(RATINGS, "u-empty", {})
    with pytest.raises(NoHistoryError):
        top_genres("u-empty")
