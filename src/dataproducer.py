"""This module represents the data producer for the project.

It is responsible for loading data pertaining to the
ranked-choice matching task and mapping this data to
custom ADTs.
"""

import random

import pandas as pd

from adt import Event, Person


def get_event_map(group: str) -> dict[str, Event]:
    """Returns a mapping of event name strings to event objects.

    Returns:
        dict[str, Event]: The event map.
    """
    data = __load_data(group, "events")
    events = list(map(__create_event, data.values.tolist()))

    return {event.name: event for event in events}


def __load_data(csv_name: str, datatype: str = "") -> pd.DataFrame:
    """Loads data from csv with specified name.

    Args:
        csv_name (str): The csv name for data retrieval.
        datatype: The type of data.

    Returns:
        pd.DataFrame: The requested data.
    """
    if datatype == "events":
        return pd.read_csv(f"events/{csv_name}.csv")

    return pd.read_csv(f"data/{csv_name}.csv")


def __create_event(row: list) -> Event:
    return Event(
        name=row[0].strip(),
        capacity=row[1],
    )


def __create_person(row: list) -> Person:
    return Person(
        name=row[1],
        email=row[0],
        choices=row[2].split(","),
        top_choice=row[3],
        placement=row[4],
    )


def get_people(group: str) -> list[Person]:
    """Returns a shuffled list of Person objects.

    Args:
        group (str): The desired group of people.

    Returns:
        list[Person]: The people in the group.
    """
    data = __load_data(group)
    data = data.fillna("")

    people = list(map(__create_person, data.values.tolist()))
    random.shuffle(people)
    return people


def main() -> None:
    """Unit Testing."""


if __name__ == "__main__":
    main()
