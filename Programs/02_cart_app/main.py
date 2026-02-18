from storage.file_storage import FileStorage
from cli import CLI

def main():

    storage = FileStorage("data/cart.json")
    cart = storage.load()

    cli = CLI(cart, storage)
    cli.run()

if __name__ == "__main__":
    main()


