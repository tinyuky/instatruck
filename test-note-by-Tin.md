# Instatruck coding test by Tin

## Python test goal

Done

## Python test Goal (legacy)

- I create a new class to store all constant in Wrapper class, make it easies to maintain in feature
- I found 1 issue: we strip data['Expiration'] as string when store it but when read from Wrapper._role_session_cache we don't convert back it to datetime object
- I have no time to implement all tests I want but I already wrote down some basic tests we must have

## Django / Django Rest Framework test goals

### 1. Convert to API which reads the sqlite database

Done. It is postman api doc

```
django/Instatruck Test.json
```

### 2. Implement a date-filtering user requirement

Done. run unitest by command

```
python manage.py test pages.tests.api.movies_api_test
```

### 3. Implement a top-10 user requirement

Done. run unitest by command

```
python manage.py test pages.tests.api.movies_api_test
```

### 4. Implement nearest-to-birthday requirement

Done. run unitest by command

```
python manage.py test pages.tests.api.actors_api_test
```

## Delivery

I added 1 more lib to fake data


