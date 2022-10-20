from pydantic import BaseModel, Field
import uuid


# class Todo(BaseModel):
#     name: str
#     description: str
#     completed: bool
#     date: str


class CrashHistory(BaseModel):
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    crash_date: str # TODO: timestamp
    crash_time: float
    borough: str # TODO: enum
    zip_code: int
    latitude: float
    longitude: float
    on_street_name: str
    cross_street_name: str
    off_street_name: str
    number_of_persons_injured: int
    number_of_persons_killed: int
    number_of_pedestrians_injured: int
    number_of_pedestrians_killed: int
    number_of_cyclist_injured: int
    number_of_cyclist_killed: int
    number_of_motorist_injured: int
    number_of_motorist_killed: int
    contributing_factor_vehicle_1: str
    contributing_factor_vehicle_2: str
    contributing_factor_vehicle_3: str
    contributing_factor_vehicle_4: str
    contributing_factor_vehicle_5: str
    contributing_factors: str
    collision_id: int
    vehicle_type_code_1: str # TODO: enum
    vehicle_type_code_2: str # TODO: enum
    vehicle_type_code_3: str # TODO: enum
    vehicle_type_code_4: str # TODO: enum
    vehicle_type_code_5: str # TODO: enum
    vehicles: str
    intersection: str
    coordinates: str
    after_pandemic: str # TODO: Boolean
    road_user_types: str # TODO: List[enum]
    day_of_week: int
    day_time: str # TODO: Boolean
    streets: str


    class Config:
        allow_population_by_field_name = True
        schema_extra = {
            "example": {
                "_id": "ObjectId(\"633b7fca8fedb4eae612362a\")",
                'CRASH DATE': '04/16/2021',
                'CRASH TIME': 1700,
                "BOROUGH": 'QUEENS',
                'ZIP CODE': 11366,
                "LATITUDE": 40.73197,
                "LONGITUDE": -73.78651,
                "LOCATION": '(40.73197, -73.78651)',
                'ON STREET NAME': '73 AVENUE',
                'CROSS STREET NAME': '184 STREET',
                'OFF STREET NAME': '',
                'NUMBER OF PERSONS INJURED': 5,
                'NUMBER OF PERSONS KILLED': 0,
                'NUMBER OF PEDESTRIANS INJURED': 0,
                'NUMBER OF PEDESTRIANS KILLED': 0,
                'NUMBER OF CYCLIST INJURED': 0,
                'NUMBER OF CYCLIST KILLED': 0,
                'NUMBER OF MOTORIST INJURED': 5,
                'NUMBER OF MOTORIST KILLED': 0,
                'CONTRIBUTING FACTOR VEHICLE 1': 'Traffic Control Disregarded',
                'CONTRIBUTING FACTOR VEHICLE 2': 'Unspecified',
                'CONTRIBUTING FACTOR VEHICLE 3': '',
                'CONTRIBUTING FACTOR VEHICLE 4': '',
                'CONTRIBUTING FACTOR VEHICLE 5': '',
                "COLLISION_ID": 4407853,
                'VEHICLE TYPE CODE 1': 'Sedan',
                'VEHICLE TYPE CODE 2': 'Station Wagon/Sport Utility Vehicle',
                'VEHICLE TYPE CODE 3': '',
                'VEHICLE TYPE CODE 4': '',
                'VEHICLE TYPE CODE 5': '',
                "intersection": '73 avenue and 184 street',
                "coordinates": '(49.1343313, -122.7124922)',
                "after_pandemic": 'True',
                "casualties_count": 10,
                "day_of_week": 4,
                "day_time": 'True',
                "streets": "['73 AVENUE', '184 STREET']",
                "contributing_factors": "['Traffic Control Disregarded']",
                "vehicles": "['Sedan', 'Station Wagon/Sport Utility Vehicle']",
                "road_user_types": "['car', 'motorist']"
            }
        }