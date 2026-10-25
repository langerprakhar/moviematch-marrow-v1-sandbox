"""Recommendation API used by the MovieMatch app."""

from moviematch.ranking import rank

RATINGS: dict[str, dict[str, int]] = {
    "u-ana": {"m01": 5, "m04": 4, "m02": 2},
    "u-ben": {"m03": 5, "m08": 4},
}


class NoHistoryError(LookupError):
    """The user has no ratings yet."""


def recommend_for_all(user_ids):
    return {user_id: recommend(user_id) for user_id in user_ids}


def recommend(user_id: str, limit: int = 3, genre: str | None = None) -> list[str]:
    ratings = RATINGS.get(user_id)
    if not ratings:
        raise NoHistoryError(user_id)
    return [movie.movie_id for movie in rank(ratings, genre)[:limit]]
