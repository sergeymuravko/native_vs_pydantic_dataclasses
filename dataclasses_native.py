from dataclasses import dataclass, asdict
from utils.timeit import timeit


@dataclass
class Article:
    title: str
    author: str
    language: str


@timeit
def creating() -> None:
    for i in range(1000000):
        Article("New title", "Author", "python")


@timeit
def convert_to_dict(article: Article) -> None:
    for i in range(1000000):
        asdict(article)


if __name__ == '__main__':
    # creating()
    # creating 1 000 000 of instances of dataclass takes ~0.444041479990 seconds
    first_article = Article("New title", "Author", "python")
    convert_to_dict(first_article)
    # Converting to dict 1 000 000 of instances of dataclass takes ~5.510993991006 seconds
