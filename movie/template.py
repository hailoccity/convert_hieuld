import json

from movie.model import *

from marshmallow import Schema, fields, ValidationError, EXCLUDE, validates


class ActorsNew(Schema):
    name = fields.Str()
    title = fields.Str()
    rank = fields.Int()
    directors = fields.List(fields.Str())


class NewMovei(Schema):
    actors = fields.Nested(ActorsNew)
    year = fields.Int()


arr_data = []
datas = [
    {
        "year": 2013,
        "actors": {
            "name": "Daniel Bruhl",
            "title": "Rush",
            "rank": 2,
            "directors": ["Ron Howard"],
        }
    }
]

check = getAll()


def getActors():
    arr_actor = []
    for i in check:

        check_data = i['info']
        if "actors" not in check_data:
            continue
        else:
            data = i['info']['actors']
            for j in range(len(data)):
                arr_actor.append(data[j])
    print(len(arr_actor))
    print(len(set(arr_actor)))
    # print(arr_actor)


if __name__ == '__main__':

    getActors()

    datas = [
        {
            "year": 2013,
            "actors": {
                "name": "Daniel Bruhl",
                "title": "Rush",
                "rank": 2,
                "directors": ["Ron Howard"],
            }
        }
    ]
# check = json.dumps(datas)
# result = NewMovei(many=True).loads(check)
# print(json.dumps(result, indent=2))
