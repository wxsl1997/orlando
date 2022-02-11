class CustomException(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str.format(f"custom exception:(message={self.message})")


def raise_exception():
    try:
        raise CustomException("test")
    except CustomException as result:

        assert result.message == "test"
    finally:
        print("execute finally method")


raise_exception()
