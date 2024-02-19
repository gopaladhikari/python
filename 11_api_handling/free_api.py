import requests


def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    res = requests.get(url)
    print(res)
    data = res.json()

    if data["sucess"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
    else:
        raise Exception("Error fetching data")


def main():
    try:
        username, country = fetch_random_user()
        print(f"Username: {username}, Country: {country}")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
