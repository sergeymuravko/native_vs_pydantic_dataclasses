from dataclasses import dataclass
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


if __name__ == '__main__':
    creating()
    # creating 1 000 000 of instances of dataclass takes ~0.444041479990 seconds
