import pygame
import json


def MapInformation():
    
    JSONPath = "Levels/Levels.JSON"

    with open(JSONPath,'r') as JSONFile:
        LevelDictionary = json.load(JSONFile)

    
    LevelSelection = "TestLevel"
    
    for Level in LevelDictionary:
        if Level["Name"] == LevelSelection:
           print("Name:", Level["Name"])
           MapName = Level["Name"]
           
           print("Image:", Level["Image"])
           MapImagePath = Level["Image"]
        
        return MapName, MapImagePath
        
        

