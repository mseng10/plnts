class Command:
    """Abstract Command class."""

    def __init__(self, key: str) -> None:
        self.key: str = key

    def process(self) -> None:
        print(f"Running {self.key} command")
