import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/carbonandmore-carbonandmore-default/api/carbonfootprint1'

mcp = FastMCP('carbonfootprint1')

@mcp.tool()
def air_quality_health_index(O3: Annotated[str, Field(description='The ground-level ozone (O3) in parts per billion (ppb).in')],
                             NO2: Annotated[str, Field(description='The nitrogen dioxide (NO2), in parts per billion (ppb)')],
                             PM: Annotated[str, Field(description='The fine particulate matter (PM2.5), PM2.5 is * measured in micrograms per cubic metre (ug/m3).')]) -> dict: 
    '''Return the official air quality health index (1 to 10) bases on key parameters.The national AQHI is based on three-hour average concentrations of ground-level ozone (O3), nitrogen dioxide (NO2), and fine particulate matter (PM2.5). O3 and NO2 are measured in parts per billion (ppb) while PM2.5 is measured in micrograms per cubic metre (ug/m3)'''
    url = 'https://carbonfootprint1.p.rapidapi.com/AirQualityHealthIndex'
    headers = {'x-rapidapi-host': 'carbonfootprint1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'O3': O3,
        'NO2': NO2,
        'PM': PM,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tree_equivalent(weight: Annotated[str, Field(description='The weight of the paper')],
                    unit: Annotated[str, Field(description='The unit (kg or lb) used for the weight')]) -> dict: 
    '''Calculate how many trees it took to create paper.'''
    url = 'https://carbonfootprint1.p.rapidapi.com/TreeEquivalent'
    headers = {'x-rapidapi-host': 'carbonfootprint1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'weight': weight,
        'unit': unit,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def traditional_hydro_to_carbon_footprint(consumption: Annotated[str, Field(description='The KWH usage of hydro.')],
                                          location: Annotated[str, Field(description='The country or continent providing the hydro. Can be any of USA, Canada, UK, Europe, Africa, LatinAmerica, MiddleEast, OtherCountry')]) -> dict: 
    '''Calculate CO2e from the use of traditional hydro provider'''
    url = 'https://carbonfootprint1.p.rapidapi.com/TraditionalHydroToCarbonFootprint'
    headers = {'x-rapidapi-host': 'carbonfootprint1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'consumption': consumption,
        'location': location,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def clean_hydro_to_carbon_footprint(energy: Annotated[str, Field(description='The source of the clean energy. Can be Solar, Wind, HydroElectric, Biomass, Geothermal, Tidal or OtherCleanEnergy')],
                                    consumption: Annotated[str, Field(description='The amount of energy consumed in KWH..')]) -> dict: 
    '''Return the CO2e in Kg from the consumption of clean hydro energy'''
    url = 'https://carbonfootprint1.p.rapidapi.com/CleanHydroToCarbonFootprint'
    headers = {'x-rapidapi-host': 'carbonfootprint1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'energy': energy,
        'consumption': consumption,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def fuel_to_co2e(type: Annotated[str, Field(description='The type can be Petrol, Diesel, LPG.')],
                 litres: Annotated[str, Field(description='The number of litres to calculate from.')]) -> dict: 
    '''Transform liters of Diesel, Petrol or LPG into CO2 Equivalent in Kg.'''
    url = 'https://carbonfootprint1.p.rapidapi.com/FuelToCO2e'
    headers = {'x-rapidapi-host': 'carbonfootprint1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'type': type,
        'litres': litres,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def carbon_footprint_from_car_travel(distance: Annotated[str, Field(description='The distance in KM.')],
                                     vehicle: Annotated[str, Field(description='The type of car, either SmallDieselCar, MediumDieselCar, LargeDieselCar, MediumHybridCar, LargeHybridCar, MediumLPGCar, LargeLPGCar, MediumCNGCar, LargeCNGCar, SmallPetrolVan, LargePetrolVan, SmallDielselVan, MediumDielselVan, LargeDielselVan, LPGVan, CNGVan, SmallPetrolCar, MediumPetrolCar, LargePetrolCar, SmallMotorBike, MediumMotorBike, LargeMotorBike')]) -> dict: 
    '''Returns the CO2e in Kg from a travel by car'''
    url = 'https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromCarTravel'
    headers = {'x-rapidapi-host': 'carbonfootprint1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'distance': distance,
        'vehicle': vehicle,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def carbon_footprint_from_flight(distance: Annotated[str, Field(description='The flight distance in KM')],
                                 type: Annotated[str, Field(description='The type of flight, any of DomesticFlight, ShortEconomyClassFlight, ShortBusinessClassFlight, LongEconomyClassFlight, LongPremiumClassFlight, LongBusinessClassFlight, LongFirstClassFlight')]) -> dict: 
    '''Calculate CO2e in Kg from a travel by air.'''
    url = 'https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromFlight'
    headers = {'x-rapidapi-host': 'carbonfootprint1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'distance': distance,
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def carbon_footprint_from_motor_bike(type: Annotated[str, Field(description='The type of motorbike, can be any of SmallMotorBike, MediumMotorBike, LargeMotorBike')],
                                     distance: Annotated[str, Field(description='The distance in KM')]) -> dict: 
    '''Returns the CO2e in Kg from a motorbike travel'''
    url = 'https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromMotorBike'
    headers = {'x-rapidapi-host': 'carbonfootprint1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'type': type,
        'distance': distance,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def carbon_footprint_from_public_transit(distance: Annotated[str, Field(description='The distance in KM.')],
                                         type: Annotated[str, Field(description='The type of transportation, one of: Taxi, ClassicBus, EcoBus, Coach, NationalTrain, LightRail, Subway, FerryOnFoot, FerryInCar')]) -> dict: 
    '''Return CO2e in Kg from the use of public transporation.'''
    url = 'https://carbonfootprint1.p.rapidapi.com/CarbonFootprintFromPublicTransit'
    headers = {'x-rapidapi-host': 'carbonfootprint1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'distance': distance,
        'type': type,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
