import pytest

from moviematch.api import NoHistoryError, recommend, recommend_for_all


def test_recommend_for_all_returns_each_users_recommendations():
    user_ids = ["u-ana", "u-ben"]

    assert recommend_for_all(user_ids) == {
        user_id: recommend(user_id) for user_id in user_ids
    }


def test_recommend_for_all_with_no_users():
    assert recommend_for_all([]) == {}


def test_recommend_for_all_propagates_no_history_error():
    with pytest.raises(NoHistoryError):
        recommend_for_all(["u-new"])
