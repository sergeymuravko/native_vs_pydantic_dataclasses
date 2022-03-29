from pydantic import BaseModel

from utils.timeit import timeit


class Article(BaseModel):
    title: str
    author: str
    language: str


@timeit
def creating() -> None:
    for i in range(1000000):
        Article(**data)


if __name__ == '__main__':
    data = {'title': 'New title', 'author': 'Author', 'language': 'python'}
    creating()
    # creating 1 000 000 of instances of dataclass takes ~5.404597358007 seconds
