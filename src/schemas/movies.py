import datetime

from pydantic import BaseModel, ConfigDict


class MovieBase(BaseModel):
    name: str
    date: datetime.date
    score: float
    overview: str


class MovieListItemSchema(MovieBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class MovieListResponseSchema(BaseModel):
    movies: list[MovieListItemSchema]
    prev_page: str | None
    next_page: str | None
    total_pages: int
    total_items: int


class MovieCreateRequestSchema(MovieBase):
    status: str
    budget: float
    revenue: float
    country: str
    genres: list[str]
    actors: list[str]
    languages: list[str]


class CountryResponseSchema(BaseModel):
    id: int
    code: str
    name: str | None

    model_config = ConfigDict(from_attributes=True)


class GenreActorLanguageResponseSchema(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)


class MovieCreateResponseSchema(MovieBase):
    id: int
    status: str
    budget: float
    revenue: float
    country: CountryResponseSchema
    genres: list[GenreActorLanguageResponseSchema]
    actors: list[GenreActorLanguageResponseSchema]
    languages: list[GenreActorLanguageResponseSchema]

    model_config = ConfigDict(from_attributes=True)


class MovieDetailSchema(MovieCreateResponseSchema):
    pass


class MovieUpdate(BaseModel):
    name: str | None = None
    date: datetime.date | None = None
    score: float | None = None
    overview: str | None = None
    status: str | None = None
    budget: float | None = None
    revenue: float | None = None
