# def todo_serializer(todo) -> dict:
#     return {
#         "id": str(todo["_id"]),
#         "name": todo["name"],
#         "description": todo["description"],
#         "completed": todo["completed"],
#         "date": todo["date"],
#     }

# def todos_serializer(todos) -> list:
#     return [todo_serializer(todo) for todo in todos]

def crashHistory_serializer(history) -> dict:
    return {
        "id": str(history["_id"]),
        "crash_date": history["CRASH_DATE"],
        "crash_time": history["CRASH_TIME"],
        "borough": history["BOROUGH"],
        "zip_code": history["ZIP_CODE"], 
        "latitude": history["LATITUDE"],
        "longitude": history["LONGITUDE"],
        "on_street_name": history["ON_STREET_NAME"],
        "cross_street_name": history["CROSS_STREET_NAME"],
        "off_street_name": history["OFF_STREET_NAME"],
        "number_of_persons_injured": history["NUMBER_OF_PERSONS_INJURED"],
        "number_of_persons_killed": history["NUMBER_OF_PERSONS_KILLED"],
        "number_of_pedestrians_injured": history["NUMBER_OF_PEDESTRIANS_INJURED"],
        "number_of_pedestrians_killed": history["NUMBER_OF_PEDESTRIANS_KILLED"],
        "number_of_cyclist_injured": history["NUMBER_OF_CYCLIST_INJURED"],
        "number_of_cyclist_killed": history["NUMBER_OF_CYCLIST_KILLED"],
        "number_of_motorist_injured": history["NUMBER_OF_MOTORIST_INJURED"],
        "number_of_motorist_killed": history["NUMBER_OF_MOTORIST_KILLED"],
        "contributing_factor_vehicle_1": history["CONTRIBUTING_FACTOR_VEHICLE_1"],
        "contributing_factor_vehicle_2": history["CONTRIBUTING_FACTOR_VEHICLE_2"],
        "contributing_factor_vehicle_3": history["CONTRIBUTING_FACTOR_VEHICLE_3"],
        "contributing_factor_vehicle_4": history["CONTRIBUTING_FACTOR_VEHICLE_4"],
        "contributing_factor_vehicle_5": history["CONTRIBUTING_FACTOR_VEHICLE_5"],
        "contributing_factors": history["contributing_factors"],
        "collision_id": history["COLLISION_ID"],
        "vehicle_type_code_1": history["VEHICLE_TYPE_CODE_1"],
        "vehicle_type_code_2": history["VEHICLE_TYPE_CODE_2"],
        "vehicle_type_code_3": history["VEHICLE_TYPE_CODE_3"],
        "vehicle_type_code_4": history["VEHICLE_TYPE_CODE_4"],
        "vehicle_type_code_5": history["VEHICLE_TYPE_CODE_5"],
        "vehicles": history["vehicles"],
        "intersection": history["intersection"],
        "coordinates": history["coordinates"],
        "after_pandemic": history["after_pandemic"],
        "road_user_types": history["road_user_types"],
        "day_of_week": history["day_of_week"],
        "day_time": history["day_time"],
        "streets": history["streets"],
        "casualties_count": history["casualties_count"],
    }

def crashHistory_list(histories) -> list:
    return [crashHistory_serializer(history) for history in histories]

def intersectionScore_serializer(history) -> dict:
    return {
        "coordinates": history["loc"],
        "contributing_factor": history["CONTRIBUTING FACTOR VEHICLE 1"],
        "casualties_count": history["casualties_count"],
        "intersection": history["intersection"]
    }

def intersectionScore_list(histories) -> list:
    return [intersectionScore_serializer(history) for history in histories]
    