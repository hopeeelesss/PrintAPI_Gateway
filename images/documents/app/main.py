import fastapi
from fastapi import FastAPI
import json

app = FastAPI()


@app.get("/documents")
async def documents(page: int = 1, amount: int = 10):
    #    with open("documents.json", 'r') as db:
    #        text = json.load(db)
    text = anus
    return text[(page - 1) * amount:page * amount]


@app.get("/headersback")
async def headersback(user_agent: str = fastapi.Header(default=None)):
    return {"User-Agent": user_agent}


#
# @app.get("/printers")
# async def show_printers(amount: int = 10, page: int = 1):
#     with open("printers.json", 'r') as db:
#         text = json.load(db)
#     return text[(page - 1) * amount:page * amount]


anus = [
    {
        "document_uuid": "636ed216b8aaf7a64eb614d2",
        "document_name": "Turner",
        "document_created": "2015-05-14T07:47:14 -03:00",
        "document_edited": "2022-01-22T04:01:11 -03:00"
    },
    {
        "document_uuid": "636ed216b6fcd6af99d94eb8",
        "document_name": "Patsy",
        "document_created": "2016-03-31T05:58:42 -03:00",
        "document_edited": "2022-11-08T03:42:57 -03:00"
    },
    {
        "document_uuid": "636ed216b8ac79f60e44235d",
        "document_name": "Elinor",
        "document_created": "2021-05-29T01:03:33 -03:00",
        "document_edited": "2022-10-02T04:10:48 -03:00"
    },
    {
        "document_uuid": "636ed216a4eb04edae1cee27",
        "document_name": "Roman",
        "document_created": "2020-06-28T12:14:58 -03:00",
        "document_edited": "2022-09-10T03:50:25 -03:00"
    },
    {
        "document_uuid": "636ed216a4fe6933d9cafb09",
        "document_name": "Cohen",
        "document_created": "2015-09-03T11:29:08 -03:00",
        "document_edited": "2022-04-24T08:29:42 -03:00"
    },
    {
        "document_uuid": "636ed216ab9e0cc62c66dfa1",
        "document_name": "Collier",
        "document_created": "2018-08-10T03:15:03 -03:00",
        "document_edited": "2022-01-23T02:53:11 -03:00"
    },
    {
        "document_uuid": "636ed216aa48743915527537",
        "document_name": "Candice",
        "document_created": "2019-10-20T06:34:52 -03:00",
        "document_edited": "2022-03-23T01:42:11 -03:00"
    },
    {
        "document_uuid": "636ed2164e7ae78e563a22c3",
        "document_name": "Patrica",
        "document_created": "2014-10-19T03:21:37 -04:00",
        "document_edited": "2022-01-24T01:22:31 -03:00"
    },
    {
        "document_uuid": "636ed21601a79be6d745a869",
        "document_name": "Deena",
        "document_created": "2022-07-04T07:58:55 -03:00",
        "document_edited": "2022-01-17T12:57:16 -03:00"
    },
    {
        "document_uuid": "636ed216bd49bbe8abbb313a",
        "document_name": "Liza",
        "document_created": "2016-03-16T10:19:36 -03:00",
        "document_edited": "2022-09-15T03:52:41 -03:00"
    },
    {
        "document_uuid": "636ed216f17816cf530a8704",
        "document_name": "Lamb",
        "document_created": "2020-08-24T04:37:05 -03:00",
        "document_edited": "2022-08-13T03:48:28 -03:00"
    },
    {
        "document_uuid": "636ed216422f0499c92baaa8",
        "document_name": "Delaney",
        "document_created": "2014-12-20T04:57:30 -03:00",
        "document_edited": "2022-10-22T04:20:12 -03:00"
    },
    {
        "document_uuid": "636ed216d268654e07e16343",
        "document_name": "Warren",
        "document_created": "2016-05-22T08:48:40 -03:00",
        "document_edited": "2022-08-30T08:11:19 -03:00"
    },
    {
        "document_uuid": "636ed216724c5a26e0eba07c",
        "document_name": "Richard",
        "document_created": "2019-09-13T12:28:28 -03:00",
        "document_edited": "2022-03-25T12:34:03 -03:00"
    },
    {
        "document_uuid": "636ed216855d17e0310381cd",
        "document_name": "Bauer",
        "document_created": "2019-06-03T12:08:33 -03:00",
        "document_edited": "2022-09-14T07:10:08 -03:00"
    },
    {
        "document_uuid": "636ed216e3b7c6baa5b6e8aa",
        "document_name": "Wright",
        "document_created": "2021-06-14T10:06:16 -03:00",
        "document_edited": "2022-03-26T12:56:27 -03:00"
    },
    {
        "document_uuid": "636ed2164dfc7fc65c57cc39",
        "document_name": "Porter",
        "document_created": "2021-04-25T10:29:03 -03:00",
        "document_edited": "2022-04-24T10:52:40 -03:00"
    },
    {
        "document_uuid": "636ed2169a54fc86c05194a3",
        "document_name": "Tonya",
        "document_created": "2016-10-15T05:28:24 -03:00",
        "document_edited": "2022-02-20T07:04:57 -03:00"
    },
    {
        "document_uuid": "636ed216773138d945826f73",
        "document_name": "Jordan",
        "document_created": "2014-12-11T05:31:24 -03:00",
        "document_edited": "2022-06-11T03:46:52 -03:00"
    },
    {
        "document_uuid": "636ed216a50be08d64205f8c",
        "document_name": "Marcia",
        "document_created": "2016-08-03T11:51:23 -03:00",
        "document_edited": "2022-03-30T06:53:32 -03:00"
    },
    {
        "document_uuid": "636ed21674b88001f1cdee79",
        "document_name": "Carrillo",
        "document_created": "2015-11-05T02:50:44 -03:00",
        "document_edited": "2022-01-17T07:11:49 -03:00"
    },
    {
        "document_uuid": "636ed21654c2e30fdc5a1cc4",
        "document_name": "Woods",
        "document_created": "2017-06-20T09:43:37 -03:00",
        "document_edited": "2022-10-07T04:29:18 -03:00"
    },
    {
        "document_uuid": "636ed216f2aa236a404f8cc4",
        "document_name": "Kathy",
        "document_created": "2018-08-05T01:34:08 -03:00",
        "document_edited": "2022-07-07T04:17:32 -03:00"
    },
    {
        "document_uuid": "636ed216b364c1c5098e6ebb",
        "document_name": "Alisa",
        "document_created": "2020-05-19T11:09:52 -03:00",
        "document_edited": "2022-03-21T10:44:55 -03:00"
    },
    {
        "document_uuid": "636ed216da61538596e7068d",
        "document_name": "Mclean",
        "document_created": "2017-02-17T01:03:36 -03:00",
        "document_edited": "2022-04-14T09:40:39 -03:00"
    },
    {
        "document_uuid": "636ed216e7d539ab0cddc37c",
        "document_name": "Benton",
        "document_created": "2016-02-06T09:18:51 -03:00",
        "document_edited": "2022-10-06T07:59:41 -03:00"
    },
    {
        "document_uuid": "636ed21631d8877cb6486d1e",
        "document_name": "Gates",
        "document_created": "2022-10-17T07:42:41 -03:00",
        "document_edited": "2022-11-07T01:37:06 -03:00"
    },
    {
        "document_uuid": "636ed216b01b96a9d784e411",
        "document_name": "Beck",
        "document_created": "2014-04-02T09:06:20 -04:00",
        "document_edited": "2022-02-08T10:12:59 -03:00"
    },
    {
        "document_uuid": "636ed21610334eb375f7e109",
        "document_name": "Shepherd",
        "document_created": "2022-07-15T06:53:35 -03:00",
        "document_edited": "2022-11-02T04:05:00 -03:00"
    },
    {
        "document_uuid": "636ed216073f25a9c72eec09",
        "document_name": "Jeanne",
        "document_created": "2015-07-06T11:15:39 -03:00",
        "document_edited": "2022-01-22T09:48:59 -03:00"
    },
    {
        "document_uuid": "636ed21695805fe2e954c6d4",
        "document_name": "Steele",
        "document_created": "2017-03-09T03:43:21 -03:00",
        "document_edited": "2022-07-27T10:09:12 -03:00"
    },
    {
        "document_uuid": "636ed216b8871c06e1231e64",
        "document_name": "Prince",
        "document_created": "2014-08-09T12:05:36 -04:00",
        "document_edited": "2022-04-24T10:26:01 -03:00"
    },
    {
        "document_uuid": "636ed216a159b2ed49e61e08",
        "document_name": "Sellers",
        "document_created": "2015-05-29T04:27:01 -03:00",
        "document_edited": "2022-09-11T12:10:13 -03:00"
    },
    {
        "document_uuid": "636ed21676edecfc04fe4b29",
        "document_name": "Jefferson",
        "document_created": "2021-09-27T06:57:28 -03:00",
        "document_edited": "2022-03-13T01:11:26 -03:00"
    },
    {
        "document_uuid": "636ed216798d7e56c028af99",
        "document_name": "Pena",
        "document_created": "2017-08-06T06:45:12 -03:00",
        "document_edited": "2022-06-13T12:18:04 -03:00"
    },
    {
        "document_uuid": "636ed216455c1cdb5275f64c",
        "document_name": "Talley",
        "document_created": "2022-01-29T12:33:50 -03:00",
        "document_edited": "2022-02-03T03:33:21 -03:00"
    },
    {
        "document_uuid": "636ed2168f8e75d22db113cd",
        "document_name": "Lizzie",
        "document_created": "2018-12-08T05:57:27 -03:00",
        "document_edited": "2022-08-18T07:20:09 -03:00"
    },
    {
        "document_uuid": "636ed216c1938017a77a45c6",
        "document_name": "Lang",
        "document_created": "2017-11-24T01:15:26 -03:00",
        "document_edited": "2022-07-15T07:15:03 -03:00"
    },
    {
        "document_uuid": "636ed21630932b5b3abd6f94",
        "document_name": "Belinda",
        "document_created": "2021-11-21T07:05:16 -03:00",
        "document_edited": "2022-03-19T03:00:28 -03:00"
    },
    {
        "document_uuid": "636ed216bbeb515144e07ee2",
        "document_name": "Mamie",
        "document_created": "2021-04-25T06:27:41 -03:00",
        "document_edited": "2022-07-20T09:01:47 -03:00"
    },
    {
        "document_uuid": "636ed216d8ea36aca3d19be7",
        "document_name": "Marquez",
        "document_created": "2022-11-10T12:59:56 -03:00",
        "document_edited": "2022-06-22T04:44:16 -03:00"
    },
    {
        "document_uuid": "636ed216ebee552bb2529768",
        "document_name": "Bettie",
        "document_created": "2019-10-29T12:43:07 -03:00",
        "document_edited": "2022-03-10T04:35:27 -03:00"
    },
    {
        "document_uuid": "636ed216743f1fb94c614aa4",
        "document_name": "Concetta",
        "document_created": "2015-08-26T12:37:02 -03:00",
        "document_edited": "2022-04-24T08:41:30 -03:00"
    },
    {
        "document_uuid": "636ed216d64ff4bf96e7dc4f",
        "document_name": "Ramona",
        "document_created": "2018-02-11T11:10:36 -03:00",
        "document_edited": "2022-06-11T10:18:37 -03:00"
    },
    {
        "document_uuid": "636ed2169335d3908579d1b7",
        "document_name": "Fischer",
        "document_created": "2016-12-27T10:02:40 -03:00",
        "document_edited": "2022-05-07T03:59:38 -03:00"
    },
    {
        "document_uuid": "636ed21628e1b688964b5032",
        "document_name": "Golden",
        "document_created": "2014-05-26T05:04:11 -04:00",
        "document_edited": "2022-08-02T10:49:58 -03:00"
    },
    {
        "document_uuid": "636ed2163ab69d8b4a77353f",
        "document_name": "Tamara",
        "document_created": "2014-08-13T08:45:53 -04:00",
        "document_edited": "2022-01-08T10:29:36 -03:00"
    },
    {
        "document_uuid": "636ed2162e1da082bd8eecfb",
        "document_name": "Denise",
        "document_created": "2019-01-10T07:12:21 -03:00",
        "document_edited": "2022-08-24T03:55:19 -03:00"
    },
    {
        "document_uuid": "636ed216715476a078b12170",
        "document_name": "Cobb",
        "document_created": "2017-11-20T12:28:35 -03:00",
        "document_edited": "2022-04-22T04:16:36 -03:00"
    },
    {
        "document_uuid": "636ed2161000dab517c2b796",
        "document_name": "Paula",
        "document_created": "2019-08-16T11:23:04 -03:00",
        "document_edited": "2022-04-01T04:36:06 -03:00"
    },
    {
        "document_uuid": "636ed216de6717161a11a9e1",
        "document_name": "Rachael",
        "document_created": "2018-10-16T07:09:02 -03:00",
        "document_edited": "2022-01-06T05:30:06 -03:00"
    },
    {
        "document_uuid": "636ed216e0e1d879620f58cd",
        "document_name": "Madge",
        "document_created": "2015-07-04T04:24:55 -03:00",
        "document_edited": "2022-06-15T07:46:09 -03:00"
    },
    {
        "document_uuid": "636ed216bb1068efe4322802",
        "document_name": "Jewell",
        "document_created": "2019-04-15T04:02:29 -03:00",
        "document_edited": "2022-04-22T01:27:03 -03:00"
    },
    {
        "document_uuid": "636ed21686ba3491870e6180",
        "document_name": "Shaffer",
        "document_created": "2015-03-06T07:36:24 -03:00",
        "document_edited": "2022-03-14T06:03:09 -03:00"
    },
    {
        "document_uuid": "636ed21618effef26a6d48a5",
        "document_name": "Marta",
        "document_created": "2014-10-01T11:29:14 -04:00",
        "document_edited": "2022-09-22T01:57:19 -03:00"
    },
    {
        "document_uuid": "636ed2165e5816d440ea7f14",
        "document_name": "Roxie",
        "document_created": "2018-04-16T06:18:01 -03:00",
        "document_edited": "2022-06-09T11:14:18 -03:00"
    },
    {
        "document_uuid": "636ed216164d40ea4a5a51a9",
        "document_name": "Clarissa",
        "document_created": "2016-08-30T05:31:40 -03:00",
        "document_edited": "2022-03-19T07:16:01 -03:00"
    },
    {
        "document_uuid": "636ed21603081ef882717aeb",
        "document_name": "Evans",
        "document_created": "2014-06-20T09:48:32 -04:00",
        "document_edited": "2022-10-30T12:47:06 -03:00"
    },
    {
        "document_uuid": "636ed2166b921d3f88c183f1",
        "document_name": "Blanche",
        "document_created": "2020-05-12T04:50:44 -03:00",
        "document_edited": "2022-04-28T10:07:00 -03:00"
    },
    {
        "document_uuid": "636ed2167cd1e82469989c93",
        "document_name": "Chase",
        "document_created": "2021-07-22T01:56:39 -03:00",
        "document_edited": "2022-02-21T05:15:07 -03:00"
    },
    {
        "document_uuid": "636ed216edd9c3f78cc98ce6",
        "document_name": "Shelton",
        "document_created": "2021-08-28T11:40:31 -03:00",
        "document_edited": "2022-04-11T11:57:04 -03:00"
    },
    {
        "document_uuid": "636ed2165b4f8fc344a687cc",
        "document_name": "Noble",
        "document_created": "2016-04-06T10:09:41 -03:00",
        "document_edited": "2022-01-03T04:21:37 -03:00"
    },
    {
        "document_uuid": "636ed216835373ea8fedb928",
        "document_name": "Padilla",
        "document_created": "2020-04-04T09:37:13 -03:00",
        "document_edited": "2022-09-23T08:31:32 -03:00"
    },
    {
        "document_uuid": "636ed216810b1804ef913fc0",
        "document_name": "Ella",
        "document_created": "2021-04-17T09:04:38 -03:00",
        "document_edited": "2022-04-08T08:52:42 -03:00"
    },
    {
        "document_uuid": "636ed216a9cf28f2c4a49e3b",
        "document_name": "Cooley",
        "document_created": "2018-11-08T02:35:50 -03:00",
        "document_edited": "2022-01-31T10:53:59 -03:00"
    },
    {
        "document_uuid": "636ed2168204a1ec6b748f68",
        "document_name": "Bird",
        "document_created": "2022-04-26T05:57:05 -03:00",
        "document_edited": "2022-04-19T06:44:07 -03:00"
    },
    {
        "document_uuid": "636ed216d0da3dfa0d4c5a69",
        "document_name": "Linda",
        "document_created": "2019-07-18T04:34:58 -03:00",
        "document_edited": "2022-04-24T09:54:27 -03:00"
    },
    {
        "document_uuid": "636ed216626b5d04fe83c5f4",
        "document_name": "Perez",
        "document_created": "2018-08-18T07:27:50 -03:00",
        "document_edited": "2022-08-18T03:44:01 -03:00"
    },
    {
        "document_uuid": "636ed2161cf39e31097dc6c1",
        "document_name": "Gracie",
        "document_created": "2014-06-22T04:12:56 -04:00",
        "document_edited": "2022-06-23T07:49:26 -03:00"
    },
    {
        "document_uuid": "636ed21617da406e940bb563",
        "document_name": "Gilliam",
        "document_created": "2017-03-15T11:35:43 -03:00",
        "document_edited": "2022-08-09T05:43:10 -03:00"
    },
    {
        "document_uuid": "636ed216f8986a3ca2864758",
        "document_name": "Kemp",
        "document_created": "2021-03-10T11:43:37 -03:00",
        "document_edited": "2022-02-10T08:56:46 -03:00"
    },
    {
        "document_uuid": "636ed216b6ec8f68167b4464",
        "document_name": "Odonnell",
        "document_created": "2020-04-04T04:38:10 -03:00",
        "document_edited": "2022-03-13T08:59:53 -03:00"
    },
    {
        "document_uuid": "636ed2164caf69dee13a783b",
        "document_name": "Jerri",
        "document_created": "2014-11-15T04:20:00 -03:00",
        "document_edited": "2022-04-21T04:39:05 -03:00"
    },
    {
        "document_uuid": "636ed2166f73a431698eff9e",
        "document_name": "Juarez",
        "document_created": "2014-11-20T02:08:52 -03:00",
        "document_edited": "2022-06-21T02:13:09 -03:00"
    },
    {
        "document_uuid": "636ed216aef9c5520f308253",
        "document_name": "Rosalinda",
        "document_created": "2017-02-05T01:07:20 -03:00",
        "document_edited": "2022-09-27T08:10:05 -03:00"
    },
    {
        "document_uuid": "636ed21637075bb2193a80f2",
        "document_name": "Beulah",
        "document_created": "2019-01-26T09:40:15 -03:00",
        "document_edited": "2022-09-05T08:47:23 -03:00"
    },
    {
        "document_uuid": "636ed21616b49dcbbd9d3321",
        "document_name": "Marina",
        "document_created": "2017-08-03T04:11:29 -03:00",
        "document_edited": "2022-03-22T12:18:12 -03:00"
    },
    {
        "document_uuid": "636ed2163320164b9a5ffcd4",
        "document_name": "Natalie",
        "document_created": "2017-11-18T07:57:16 -03:00",
        "document_edited": "2022-03-23T04:20:34 -03:00"
    },
    {
        "document_uuid": "636ed2163bd93fc86e7e7964",
        "document_name": "Burns",
        "document_created": "2019-04-11T12:10:46 -03:00",
        "document_edited": "2022-04-04T02:09:11 -03:00"
    },
    {
        "document_uuid": "636ed2169ffd0a7c1b683338",
        "document_name": "Estela",
        "document_created": "2022-04-27T04:15:08 -03:00",
        "document_edited": "2022-09-04T10:51:36 -03:00"
    },
    {
        "document_uuid": "636ed2168a21879d28d2b0f9",
        "document_name": "Colon",
        "document_created": "2014-05-23T07:35:55 -04:00",
        "document_edited": "2022-04-13T08:42:31 -03:00"
    },
    {
        "document_uuid": "636ed216a4e01d264824122b",
        "document_name": "Mcclure",
        "document_created": "2015-10-08T10:09:10 -03:00",
        "document_edited": "2022-11-06T08:36:14 -03:00"
    },
    {
        "document_uuid": "636ed216081a911ee3cc7c19",
        "document_name": "Emerson",
        "document_created": "2022-01-21T11:57:55 -03:00",
        "document_edited": "2022-08-23T02:30:25 -03:00"
    },
    {
        "document_uuid": "636ed2166a40bb4809f3de7b",
        "document_name": "Angela",
        "document_created": "2022-08-06T04:59:17 -03:00",
        "document_edited": "2022-06-11T07:59:51 -03:00"
    },
    {
        "document_uuid": "636ed216cd56c65f7361b0c8",
        "document_name": "Ross",
        "document_created": "2017-10-20T09:28:36 -03:00",
        "document_edited": "2022-10-11T06:04:51 -03:00"
    },
    {
        "document_uuid": "636ed216f69c678900ca149a",
        "document_name": "Laurel",
        "document_created": "2015-04-12T10:42:38 -03:00",
        "document_edited": "2022-04-03T02:37:32 -03:00"
    },
    {
        "document_uuid": "636ed2169a01e0408a22dda5",
        "document_name": "Ollie",
        "document_created": "2017-12-31T12:46:40 -03:00",
        "document_edited": "2022-08-27T04:57:07 -03:00"
    },
    {
        "document_uuid": "636ed21682f0f3b6f9812d9c",
        "document_name": "Johns",
        "document_created": "2021-02-21T10:29:18 -03:00",
        "document_edited": "2022-08-10T11:58:43 -03:00"
    },
    {
        "document_uuid": "636ed21610256fecdb24155e",
        "document_name": "Peggy",
        "document_created": "2021-08-07T07:29:04 -03:00",
        "document_edited": "2022-01-24T09:07:19 -03:00"
    },
    {
        "document_uuid": "636ed216139ef628a264e95b",
        "document_name": "Pamela",
        "document_created": "2016-08-19T08:38:37 -03:00",
        "document_edited": "2022-06-03T09:30:35 -03:00"
    },
    {
        "document_uuid": "636ed216bf42067e2caf0fe5",
        "document_name": "Rutledge",
        "document_created": "2021-06-04T02:22:42 -03:00",
        "document_edited": "2022-01-14T01:33:58 -03:00"
    },
    {
        "document_uuid": "636ed216daabcc00a3c3a9b3",
        "document_name": "Lois",
        "document_created": "2015-05-18T06:44:22 -03:00",
        "document_edited": "2022-04-05T05:01:56 -03:00"
    },
    {
        "document_uuid": "636ed216100d56bb08f63df8",
        "document_name": "Hoover",
        "document_created": "2017-10-02T02:21:33 -03:00",
        "document_edited": "2022-10-10T02:56:47 -03:00"
    },
    {
        "document_uuid": "636ed2167051f7a81cadac7c",
        "document_name": "Carver",
        "document_created": "2016-09-05T02:06:43 -03:00",
        "document_edited": "2022-04-18T06:42:08 -03:00"
    },
    {
        "document_uuid": "636ed216636f9d9a498c71b4",
        "document_name": "Alston",
        "document_created": "2017-08-12T10:21:06 -03:00",
        "document_edited": "2022-07-21T09:05:53 -03:00"
    },
    {
        "document_uuid": "636ed216ac1cc3ebc328acac",
        "document_name": "Newman",
        "document_created": "2018-11-24T04:11:37 -03:00",
        "document_edited": "2022-06-26T09:01:33 -03:00"
    },
    {
        "document_uuid": "636ed21679f3e9807a15cc45",
        "document_name": "Josefina",
        "document_created": "2016-10-25T08:10:28 -03:00",
        "document_edited": "2022-03-05T02:29:33 -03:00"
    },
    {
        "document_uuid": "636ed216e6cb603a90c28a2c",
        "document_name": "Mosley",
        "document_created": "2018-01-09T12:53:58 -03:00",
        "document_edited": "2022-04-18T05:59:14 -03:00"
    },
    {
        "document_uuid": "636ed2165bb32f99f1bb0fc6",
        "document_name": "Fulton",
        "document_created": "2017-09-02T02:53:39 -03:00",
        "document_edited": "2022-04-05T02:09:39 -03:00"
    },
    {
        "document_uuid": "636ed2167fb93038506ba12f",
        "document_name": "Rosanne",
        "document_created": "2022-01-16T02:18:02 -03:00",
        "document_edited": "2022-06-01T07:28:44 -03:00"
    }
]
