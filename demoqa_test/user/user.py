import dataclasses

@dataclasses.dataclass()
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    user_number: str
    year: str
    month: str
    day: str
    subjects: str
    hobbies: str
    test_upload_file: str
    address: str
    state: str
    city: str
