"""Recommendation API used by the MovieMatch app."""

from moviematch.ranking import rank

RATINGS: dict[str, dict[str, int]] = {
    "u-ana": {"m01": 5, "m04": 4, "m02": 2},
    "u-ben": {"m03": 5, "m08": 4},
}


class NoHistoryError(LookupError):
    """The user has no ratings yet."""


def top_genres(user_id: str) -> list[str]:
    """Return the user's genres in descending affinity order."""
    from moviematch.ranking import genre_affinity

    ratings = RATINGS.get(user_id)
    if not ratings:
        raise NoHistoryError(user_id)
    return [genre for genre, _ in genre_affinity(ratings).most_common()]


def recommend(user_id: str, limit: int = 3, genre: str | None = None) -> list[str]:
    ratings = RATINGS.get(user_id)
    if not ratings:
        raise NoHistoryError(user_id)
    return [movie.movie_id for movie in rank(ratings, genre)[:limit]]
