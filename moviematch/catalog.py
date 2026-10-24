"""Fictional movie catalog for the MovieMatch Marrow v1 sandbox."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Movie:
    movie_id: str
    title: str
    genres: tuple[str, ...]
    popularity: int


CATALOG: tuple[Movie, ...] = (
    Movie("m01", "Orbit of Ashes", ("scifi", "drama"), 91),
    Movie("m02", "The Quiet Harbor", ("drama",), 64),
    Movie("m03", "Laugh Track Ltd.", ("comedy",), 77),
    Movie("m04", "Night Ferry", ("thriller",), 83),
    Movie("m05", "Paper Dragons", ("animation", "family"), 88),
    Movie("m06", "Second Sunrise", ("romance", "drama"), 58),
    Movie("m07", "Static Bloom", ("scifi", "thriller"), 72),
    Movie("m08", "Grandma's Garage Band", ("comedy", "family"), 69),
)

BY_ID = {movie.movie_id: movie for movie in CATALOG}
