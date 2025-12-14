from typing import Union
from functools import reduce


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        def is_valid(movie: dict) -> bool:
            rating = movie["rating_kinopoisk"]
            country = movie["country"]

            return rating and float(rating) > 0 and country and len(country.split(",")) >= 2

        filtered_movies = list(filter(is_valid, list_of_movies))
        total_rating = reduce(
            lambda acc, movie: acc + float(movie["rating_kinopoisk"]), filtered_movies, 0.0
        )

        return total_rating / len(filtered_movies)

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        def count_letters(movie: dict) -> int:
            try:
                rating_kinopoisk = float(movie.get("rating_kinopoisk", 0))
            except (TypeError, ValueError):
                return 0

            if rating_kinopoisk < rating:
                return 0

            return movie.get("name", "").count("и")

        return sum(map(count_letters, list_of_movies))
