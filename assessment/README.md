## Info:

Hi!

Had hard time with Docker - it wasn't installed on my own laptop at time of assignment, and had some errors during installation. Started clear project in order to not wasting time. At some point figured out that there are old Docker files in the system (from previous installations) that interrupts the process. Found and deleted them by hands - used only for Postgresql.

If the fact that i didn't use prepared for assignment "base project" will not be acceptable - i would understand. If that's the case, i would appreciate any feedback.

I didn't work with JsonField before, so it took some time to research. My initial idea was just to store every possible value in CharField, we have a few parts like that in my current company, but i wasn't sure if it's ok, so decided to try JsonField.

I used pyenv for Python version management and virtual environment. JsonSchema to validate the JSON against the schema.
Also i used Postman to test endpoints.

Really wanted to add tests but since i felt that i ran out of time, decided not to implement it.


## Time:

I didn't measure time on purpose, but i would say it took 3-4 hours. I didn't work on that at a stretch, had to do breaks.


## Payload:

Endpoint:
http://127.0.0.1:8000/post_objects/
Payload:
```json
{
    "batch_id": "71a8a97591894dda9ea1a372c89b7987",
    "objects": [
        {
            "object_id": "48011705d5074addaecaaff237627564",
            "data": [
                {
                    "key": "type",
                    "value": "jersey"
                },
                {
                    "key": "color",
                    "value": null
                },
                {
                    "key": "size",
                    "value": "S"
                },
                {
                    "key": "demo",
                    "value": true
                },
                {
                    "key": "cost",
                    "value": 323.21
                }
            ]
        },
        {
            "object_id": "95d56ca903324809820a11c55f3826ee",
            "data": [
                {
                    "key": "color",
                    "value": "black"
                },
                {
                    "key": "size",
                    "value": "L"
                },
                {
                    "key": "country",
                    "value": "MX"
                }
            ]
        }
        
]
}
```


Endpoint:
http://127.0.0.1:8000/get_obejct_by_id/48011705d5074addaecaaff237627564
Payload:


Endpoint:
http://127.0.0.1:8000/get_obejct_by_params/
Payload:
```json
[
    {
        "key":"type"
    },
    {
        "value":"L"
    }
]
```


## To do:
-- Type hints

-- Management command for quick fill the db with test data

-- Handle duplicates

-- Tests

-- Create logs for requests and responses
