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


@timeit
def convert_to_dict(article: Article) -> None:
    for i in range(1000000):
        article.dict()


@timeit
def get_attribute(article: Article) -> None:
    for i in range(1000000):
        _ = article.title


@timeit
def set_attribute(article: Article) -> None:
    for i in range(1000000):
        article.title = 'abc'


if __name__ == '__main__':
    data = {'title': 'New title', 'author': 'Author', 'language': 'python'}
    # creating()
    # creating 1 000 000 of instances of dataclass takes ~5.404597358007 seconds
    first_article = Article(**data)
    # convert_to_dict(first_article)
    # Converting to dict 1 000 000 of instances of dataclass takes ~5.175302796008 seconds
    get_attribute(first_article)
    # Get attribute value 1 000 000 of instances of dataclass takes ~0.049166930999 seconds
    set_attribute(first_article)
    # Set attribute value 1 000 000 of instances of dataclass takes ~0.538404490000 seconds
