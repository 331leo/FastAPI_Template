## FastAPI Boilerplate

**_This Project uses [Poetry Package Manager](https://github.com/python-poetry/poetry)_**

```bash
poetry install
```

### Run Server via uvicorn (Development)

```bash
poetry run uvicorn app:app --reload
```

### Run Server via gunicorn (Production)

```bash
(Configure Appliction Settings on gunicorn.conf.py)
poetry run gunicorn app:app
```
