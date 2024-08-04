"""This module contains the Person Abstract Datatype (ADT).

This class wraps typical spreadsheet information
associated with a person for the ranked-choice matching
task.

Typical usage example:

person = Person(
    name="John Doe",
    email="jd0000@123mail.com",
    choices=["choice_1", "choice_2", "choice_3"],
    top_choice="choice_1",
)
"""

from dataclasses import dataclass


@dataclass(slots=True)
class Person:
    """Wraps the information associated with a person."""

    name: str
    "The person's name. Instance Variable."
    email: str
    "The person's unique identifier/email. Instance Variable."
    choices: list[str]
    "The person's event choices' names. Instance Variable."
    top_choice: str
    "The person's top_choice event name. Instance Variable."
    placement: str = ""
    "The person's placed event name. Optional. Instance Variable."

    def __str__(self) -> str:
        """Returns a string representation of the person.

        Returns:
            str: Person's information.
        """
        return f"""Name: {self.name}
ID: {self.email}
Choices: {self.choices}
Top Choice: {self.top_choice}
Placement: {self.placement}"""


def main() -> None:
    """Unit Testing."""
    person = Person(
        name="John Doe",
        email="jd0000",
        choices=["Gathering 1", "Gathering 2"],
        top_choice="Gathering 1",
    )
    print(person)


if __name__ == "__main__":
    main()
