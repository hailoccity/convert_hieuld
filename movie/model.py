import json
from validation import validate_year

from marshmallow import Schema, fields, ValidationError, EXCLUDE, validates, post_load


class Movie:
    def __init__(self, year, title, info):
        self.year = year
        self.title = title
        self.info = info

    # def convert(self):
    #     self.year = MovieSchema.year
    #     self.title = MovieSchema.title
    #     self.info = Info.convert_info


# class Info:
#     def __init__(self, directors, release_date, rating, genres, image_url, plot, rank, running_time_secs, actors):
#         self.directors = directors
#         self.release_date = release_date
#         self.rating = rating
#         self.genres = genres
#         self.image_url = image_url
#         self.plot = plot
#         self.rank = rank
#         self.running_time_secs = running_time_secs
#         self.actors = actors
#
#     def convert_info(self):
#         self.directors = InfoSchema.directors
#         self.release_date = InfoSchema.release_date
#         self.rating = InfoSchema.rating
#         self.genres = InfoSchema.genres
#         self.image_url = InfoSchema.image_url
#         self.plot = InfoSchema.plot
#         self.rank = InfoSchema.rank
#         self.running_time_secs = InfoSchema.running_time_secs
#         self.actors = InfoSchema.actors
class BaseModel(Schema):
    __model__ = Movie

    @post_load()
    def make_object(self, data, **kwargs):
        return self.__model__(**data)


# class InfoSchema(Schema):
#     __model__ = Movie
#     directors = fields.List(fields.Str())
#     release_date = fields.DateTime()
#     rating = fields.Float()
#     genres = fields.List(fields.Str())
#     image_url = fields.URL()
#     plot = fields.Str()
#     rank = fields.Int()
#     running_time_secs = fields.Int()
#     actors = fields.List(fields.Str())
#
#     @post_load
#     def test(self, data, **kwargs):
#         return Movie(**data)


class MovieSchema(BaseModel):
    year = fields.Int(validate=validate_year)
    title = fields.Str()
    info = fields.Str()


data_test = [
    {
        "year": 2013,
        "title": "Rush",
        "info": {
            "directors": ["Ron Howard"],
            "release_date": "2013-09-02T00:00:00Z",
            "rating": 8.3,
            "genres": [
                "Action",
                "Biography",
                "Drama",
                "Sport"
            ],
            "image_url": "http://ia.media-imdb.com/images/M/MV5BMTQyMDE0MTY0OV5BMl5BanBnXkFtZTcwMjI2OTI0OQ@@._V1_SX400_.jpg",
            "plot": "A re-creation of the merciless 1970s rivalry between Formula One rivals James Hunt and Niki Lauda.",
            "rank": 2,
            "running_time_secs": 7380,
            "actors": [
                "Daniel Bruhl",
                "Chris Hemsworth",
                "Olivia Wilde"
            ]
        }
    }
]
fake_data = [
    {
        "year": 2013,
        "title": "Rush",
        "info": "le Hieu"
    }
]


def getData():
    movies_schema = MovieSchema()
    movies = [Movie(2021, title="Hello", info="Hieu le"),
              Movie(2020, title="Omi", info="Doan Duong")]
    show = movies_schema.dump(movies, many=True)
    movie_obj = movies_schema.load(show, many=True)
    print(movie_obj)


def getAll():
    dir_movie = r"..\..\convert_json\data\moviedata.json"
    try:

        with open(dir_movie, 'rb') as file:
            data_test = file.read()
        obj = json.loads(data_test)
        check = MovieSchema(many=True).load(obj)
        return check
        # for element in check:
        #     print(element)

        # checks = json.dumps(check, indent=2)
        # print(check)
    except ValidationError as e:
        print(e.messages)


# def getActors():
#     arr_actor = []
#     for i in check:
#
#         check_data = i['info']
#         if "actors" not in check_data:
#             continue
#         else:
#             data = i['info']['actors']
#             for j in range(len(data)):
#                 arr_actor.append(data[j])
#     print(len(arr_actor))
#     print(len(set(arr_actor)))
#     # print(arr_actor)


if __name__ == '__main__':
    getData()
