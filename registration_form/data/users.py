import dataclasses
from enum import Enum
from typing import List


class Gender(Enum):
    male = 'Male'
    female = 'Female'
    other = 'Other'


class Subject(Enum):
    chemistry = 'Chemistry'
    computer_science = 'Computer Science'
    biology = 'Biology'


class Hobbies(Enum):
    sport = 'Sport'
    reading = 'Reading'
    music = 'Music'


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: List[Gender]
    mobile_number: str
    birthday: str
    subjects: List[Subject]
    hobbies: List[Hobbies]
    picture: str
    current_address: str
    state: str
    city: str
