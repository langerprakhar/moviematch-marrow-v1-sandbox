"""Genre-affinity ranking from a user's own ratings."""

from collections import Counter

from moviematch.catalog import BY_ID, CATALOG, Movie


def genre_affinity(ratings: dict[str, int]) -> Counter:
    affinity: Counter = Counter()
    for movie_id, stars in ratings.items():
        for genre in BY_ID[movie_id].genres:
            affinity[genre] += stars - 3
    return affinity


def rank(ratings: dict[str, int], genre: str | None = None) -> list[Movie]:
    affinity = genre_affinity(ratings)
    candidates = [m for m in CATALOG if m.movie_id not in ratings]
    if genre is not None:
        candidates = [m for m in candidates if genre in m.genres]
    return sorted(
        candidates,
        key=lambda m: (-sum(affinity[g] for g in m.genres), -m.popularity, m.movie_id),
    )
