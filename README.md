# Tasty Food Search

### Quick Start

Clone the repo

```
$ git clone https://github.com/Sourabhchrs93/tasty_food_api.git
```

Initialize and activate a virtualenv:

```
$ virtualenv -p python3 env
$ source env/bin/activate
```

Install the dependencies:

```
$ pip install -r requirements.txt
```

Run the development server:

```
$ cd src
$ python apps.py
```

Navigate to `[http://localhost:8000]`

Comments:
```
- postman collection added at root for reference

- download finefoods.txt from:
  http://snap.stanford.edu/data/finefoods.txt.gz
  
- place finefoods.txt in src folder

- NOTE: some of the entries in finefoods.txt are not consistent,
        code might break while accessing such entries, clean it manually
```