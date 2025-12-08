import requests


response = requests.post(
    "http://127.0.0.1:8080/advertisement",
    json={
        "title": "Дрель",
        "description": "Качественный",
        "price": 4.01,
        "creator": "Igor",
    },
)
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/advertisement/1",
)
print(response.status_code)
print(response.json())


response = requests.post(
    "http://127.0.0.1:8080/advertisement",
    json={
        "title": "Рюкзак",
        "description": "Красный",
        "price": 10.33,
        "creator": "Ivan",
    },
)
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/advertisement/1",
)
print(response.status_code)
print(response.json())


response = requests.patch("http://127.0.0.1:8080/advertisement/1", json={
    "title": "Дрель",
    "price": 6.01,
})
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/advertisement/1",
)
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/advertisement/2",
)
print(response.status_code)
print(response.json())


response = requests.delete(
    "http://127.0.0.1:8080/advertisement/2",
)
print(response.status_code)
print(response.json())



response = requests.get(
    "http://127.0.0.1:8080/advertisement/2",
)
print(response.status_code)
print(response.json())


response = requests.post(
    "http://127.0.0.1:8080/advertisement",
    json={
        "title": "Шапка",
        "description": "В хорошем состоянии",
        "price": 1.02,
        "creator": "Igor",
    },
)
print(response.status_code)
print(response.json())


response = requests.post(
    "http://127.0.0.1:8080/advertisement",
    json={
        "title": "Шуруповерт",
        "description": "Хорошее состояние",
        "price": 6.01,
        "creator": "Victor",
    },
)
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/advertisement",
)
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/advertisement?title=Дрель",
)
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/advertisement?description=сост",
)
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/advertisement?price=6.01",
)
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/advertisement?creator=Victor",
)
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/advertisement?description=сост&price=1.02",
)
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/advertisement?creator=Ivan",
)
print(response.status_code)
print(response.json())
