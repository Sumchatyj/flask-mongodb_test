# flask-mongodb_test

## Description

This is a small flask app. It's an API service to do some CRUD operations with MongoDB database.

## Getting started

### Dependencies

* Python > 3.11
* Flask > 2.2.2

### Installing

Be sure that you have installed MongoDB before starting the app!

Clone repository and make venv with poetry or just like this:

```
python3 -m venv venv
```

And activate it:

```
source venv/bin/activate
```

Install requirements:

```
pip install -r requirements.txt
```

### Endpoins:

http://127.0.0.1:5000/users
http://127.0.0.1:5000/users/<user_id>

### Response example:

```
[
    {
        "_id": {
            "$oid": "id"
        },
        "username": "username",
        "password": "password",
        "age": age
    },
]
```
