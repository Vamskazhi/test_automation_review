class IsContainerType(Exception):
    def __init__(self, message: str = "Unexpected type"):
        super().__init__(message)
        self.msgfmt = message


class TypeKeysError(Exception):
    def __init__(
        self, message: str = "Cannot sort dictionary: keys are different types"
    ):
        super().__init__(message)
        self.msgfmt = message
