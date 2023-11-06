class Command:
    """Abstract Command class."""

    def __init__(self, key: str, description: str = "No description provided.") -> None:
        self.key: str = key
        self.description = description

    def __repr__(self):
        return f"{self.key} - {self.description}"

    def process(self) -> None:
        print(f"Running {self.key} command")
