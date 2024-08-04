"""This module contains various metrics/evaluation functions for the matching script.

The module's metric include high satisfaction percentage and general
satisfaction percentage.
"""

import pandas as pd
from adt import Event, Person


def get_high_satisfaction_percentage(
    people: list[Person],
    event_map: dict[str, Event],
) -> str:
    """Returns the high satisfaction percentage.

    The high satisfaction percentage is defined as the number of
    people that received their top choice divided by the total
    number of people.

    Args:
        people (list[Person]): People assigned events.
        event_map (dict[str, Event]): event_map with events after assignment.

    Returns:
        str: The high satisfaction metric.
    """
    top_choice_count = 0

    for person in people:
        goal_roster = event_map[person.top_choice].get_roster()
        if person in goal_roster:
            top_choice_count += 1

    return f"High Satisfaction Rating: {((top_choice_count/len(people))*100):.2f}"


def get_general_satisfaction_percentage(
    people: list[Person],
    event_map: dict[str, Event],
) -> str:
    """Returns the general satisfaction percentage.

    The general satisfaction percentage is defined as the number of
    people that received their one of their choice divided by the total
    number of people.

    Args:
        people (list[Person]): People assigned events.
        event_map (dict[str, Event]): event_map with events after assignment.

    Returns:
        str: The general satisfaction metric.
    """
    choice_count = 0

    for person in people:
        for choice in person.choices:
            roster = event_map[choice].get_roster()
            if person in roster:
                choice_count += 1
                break

    return f"General Satisfaction Rating: {((choice_count/len(people))*100):.2f}"


def count_unplaced(people: list[Person]) -> int:
    """Counts the number of unplaced individuals.

    Args:
        people (list[Person]): People placed into events.

    Returns:
        int: number of unplaced people.
    """
    count = 0
    for person in people:
        if not person.placement:
            count += 1

    return count


def collect_unhappy(people: list[Person]) -> list[Person]:
    """Returns unhappy people.

    Args:
        people (list[Person]): The people placed into events.

    Returns:
        list[Person]: The unhappy people.
    """
    return [person for person in people if person.placement not in person.choices]


def write_results(csv_name: str, event_map: dict[str, Event]) -> None:
    """Writes the resulting assignments to a csv file.

    Args:
        csv_name (str): Name of csv.
        event_map (dict[str, Event]): Events
    """
    results = []
    for event in event_map.values():
        roster = event.get_roster()
        results.extend(
            [(person.name, person.email, person.placement) for person in roster],
        )
    df = pd.DataFrame(results, columns=["name", "email", "placement"])
    df.to_csv(f"results/{csv_name}_assignments.csv", index=False)


def main() -> None:
    """Unit Testing."""


if __name__ == "__main__":
    main()
