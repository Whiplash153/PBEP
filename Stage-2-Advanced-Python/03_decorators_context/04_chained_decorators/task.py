from chained_decorators import logger, authenticate

@logger
@authenticate
def secure_action():
    print("Sensitive action performed!")

secure_action(True)
secure_action(False)
