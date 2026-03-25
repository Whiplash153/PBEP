import requests

def main():
    response = requests.get("https://httpbin.org/get")
    if response.status_code == 200:
        print("Poetry works! Request successful.")
    else:
        print("Something went wrong")

if __name__ == "__main__":
    main()