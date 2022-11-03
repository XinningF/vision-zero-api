from fastapi import APIRouter, Query
from models.crashHistory_model import CrashHistory
from config.database import collection_name, intersection_dangerousity
from schemas.crashHistory_schema import crashHistory_list, crashHistory_serializer, intersectionScore_list
from bson import ObjectId
from datetime import date, datetime
from typing import Union

api_router = APIRouter()

@api_router.get("/")     
async def get_histories():
    # histories = crashHistory_list(collection_name.find())
    return crashHistory_list(collection_name.find(limit=1))
    # return list(collection_name.find_one({"LATITUDE": 40.885784}))

# @api_router.get("/test/")
# async def test(dayOfWeek:Union[int, None] = None, isAfterPandemic:Union[bool, None] = None):
#     queryList = []
#     if dayOfWeek:
#         queryList.append({"day_of_week": dayOfWeek})
#     if isAfterPandemic:
#         queryList.append({"after_pandemic": isAfterPandemic})
    
#     print(queryList)
#     if not queryList:
#         return crashHistory_list(collection_name.find(limit=1)) 
#     return crashHistory_list(collection_name.find({"$and": queryList})) 

# TODO: date data type
@api_router.get("/getCrashHistory/")
async def get_history_date( startDate: Union[str, None] = None, endDate: Union[str, None] = None, startTime: Union[int, None] = None, endTime: Union[int, None] = None, 
                            borough: Union[str, None] = None, zipcode: Union[int, None] = None, latitude: Union[float, None] = None, longitude:Union[float, None] = None, 
                            streets: Union[list[str], None] = Query(default = None), numInjured:Union[int, None] = None, numKilled:Union[int, None] = None, numPedInjured:Union[int, None] = None, 
                            numPedKilled:Union[int, None] = None, numCycInjured:Union[int, None] = None, numCycKilled:Union[int, None] = None, 
                            numMotorInjured:Union[int, None] = None, numMotorKilled:Union[int, None] = None, contributing_factors:Union[list[str], None] = Query(default = None), vehicles:Union[list[str], None] = Query(default = None),
                            coordinates:Union[str, None] = None, numCasualties:Union[float, None] = None, dayOfWeek:Union[int, None] = None, isDayTime:Union[bool, None] = None, 
                            roadUserTypes:Union[str, None] = None, isAfterPandemic:Union[bool, None] = None
                          ):

    queryDict = []
    # DATE
    if startDate and endDate:
        [startm, startd, starty] = startDate.split("/")
        [endm, endd, endy] = endDate.split("/")
        startDateTime = datetime(int(starty), int(startm), int(startd), 0, 0, 0, 0)
        endDateTime = datetime(int(endy), int(endm), int(endd), 0, 0, 0, 0)

        queryDict.append({"CRASH_DATE": {"$gte": startDateTime, "$lte": endDateTime}})
    else:
        if startDate:
            [m, d, y] = startDate.split("/")
            startDateTime = datetime(int(y), int(m), int(d), 0, 0, 0, 0)
            queryDict.append({"CRASH_DATE": {"$gte": startDateTime}})
        if endDate:
            [m, d, y] = endDate.split("/")
            endDateTime = datetime(int(y), int(m), int(d), 0, 0, 0, 0)
            queryDict.append({"CRASH_DATE": {"$lte": endDateTime}})
    
    if startTime and endTime:
        timeQuery = {"CRASH_TIME": {"$gte": startTime, "$lte": endTime}}
        queryDict.append(timeQuery)
    else:
        if startTime:
            queryDict.append({"CRASH_TIME": {"$gte": startTime}})
        if endTime:
            queryDict.append({"CRASH_TIME": {"$lte": endTime}})

    if borough:
        boroughQuery = {"BOROUGH": {"$regex" : borough , "$options" : "i"}}
        queryDict.append(boroughQuery)

    if zipcode:
        queryDict.append({"ZIP_CODE": zipcode})

    if streets:
        for street in streets:
            queryDict.append({"streets":  {"$regex" : street , "$options" : "i"}})

    if numInjured:
        queryDict.append({"NUMBER_OF_PERSONS_INJURED": numInjured})

    if numKilled:
        queryDict.append({"NUMBER_OF_PERSONS_KILLED": numKilled})
    
    if numPedInjured:
        queryDict.append({"NUMBER_OF_PEDESTRIANS_INJURED": numPedInjured})

    if numPedKilled:
        queryDict.append({"NUMBER_OF_PEDESTRIANS_KILLED": numPedKilled})

    if numCycInjured:
        queryDict.append({"NUMBER_OF_CYCLIST_INJURED": numCycInjured})
        
    if numCycKilled:
        queryDict.append({"NUMBER_OF_CYCLIST_KILLED": numCycKilled})

    if numMotorInjured:
        queryDict.append({"NUMBER_OF_MOTORIST_INJURED": numMotorInjured})

    if numMotorKilled:
        queryDict.append({"NUMBER_OF_MOTORIST_KILLED": numMotorKilled})

    if contributing_factors:
        for factor in contributing_factors:
            queryDict.append({"contributing_factors":  {"$regex" : factor , "$options" : "i"}})
        # TODO: think about substring of input?

    if vehicles:
        for vehicle in vehicles:
            queryDict.append({"vehicles":  {"$regex" : vehicle , "$options" : "i"}})
        
    # if coordinates:
    #     coordinatesQuery = {}
    #     # TODO 

    if numCasualties:
        queryDict.append({"casualties_count": numCasualties})

    if dayOfWeek:
        queryDict.append({"day_of_week": dayOfWeek})

    if isDayTime:
        queryDict.append({"day_time": isDayTime})
    
    if roadUserTypes:
        for roadUserType in roadUserTypes:
            queryDict.append({"road_user_types":  {"$regex" : roadUserType , "$options" : "i"}})

    if isAfterPandemic:
        queryDict.append({"after_pandemic": isAfterPandemic})


    if latitude and longitude:
        queryDict.append({"loc": {"$within": {"$center": [[latitude, longitude], 0.0005]}}})
        
    elif (latitude and not longitude):
        return {"error": "Missing longitude"}
    elif (not latitude and longitude):
        return {"error": "Missing latitude"}

    if not queryDict:
        return {"error":"No input. If want to see all results, try /"} 

    return crashHistory_list(collection_name.find({"$and": queryDict})) 


@api_router.get("/positionScore/")     
async def get_score(longitude: float, latitude: float):
    if not longitude or not latitude:
        return {"error": "please input position information: [latitude, longitude]"}
        
    position = intersection_dangerousity.find({"loc": {"$within": {"$center": [[longitude, latitude], 0.0005]}}})
    if not position: return {"error": "No data nearby. Please search for another position."}

    return intersectionScore_list(position) 