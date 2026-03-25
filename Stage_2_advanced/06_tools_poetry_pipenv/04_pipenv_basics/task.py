import requests

def main():
    response = requests.get("https://httpbin.org/get")
    print("Status:", response.status_code)

if __name__ == "__main__":
    main()