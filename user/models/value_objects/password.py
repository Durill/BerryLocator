from dataclasses import dataclass

__all__ = ("Password",)


@dataclass(frozen=True)
class Password:
    first_repetition: str
    second_repetition: str

    def __post_init__(self):
        if self.first_repetition != self.second_repetition:
            print("Given Passwords are not equal")
            raise ValueError()

        if len(self.first_repetition) < 8:
            print("Given Password are too short, have to be longer than 8")
            raise ValueError()
