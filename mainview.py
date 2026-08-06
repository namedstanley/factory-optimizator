from controller.processhandler import ProcessHandler
from controller.productionplanner import ProductionPlanner

from model.cars.convertible import *
from model.cars.coupe import *
from model.cars.hatchback import *
from model.cars.sedan import *
from model.cars.suv import *
from model.cars.van import *

import PySimpleGUI as sg

def generateLot():
    pp = ProductionPlanner()
    return pp.generateProductionLot()

def createVehicles(lot):
    ph = ProcessHandler()
    vehicles = []
    for vehicle in lot:
        vehicles.append(ph.createVehicle(vehicle))
    return vehicles
    

#Global variables
LOT = []
LOT_SUMMARY = None

#Generate Production LOT graphics
gplGenerateButton = sg.Button("Generate", key="-GENPRODLOTBUTTON-")

generateProductionLotLayout = [
    [sg.Text("Lot summary")],
    [sg.Table(headings=["Car type", "Amount", "Premium", "Tuned"], values=[], key="-LOTSUM-", expand_x=True)],
    [sg.Col(expand_y=True, layout=[[]])],
    [gplGenerateButton]
]

gplTab = sg.Tab("Generate Production Lot",generateProductionLotLayout)


#Create Vehicles graphics
cvCreateButton = sg.Button("Generate", key="-CREATEVEHICLESBUTTON-")
createVehiclesLayout = [
    [sg.Text("Vehicle list")],
    [sg.Table(headings=["VIN", "Price", "HP", "Capacity", "Production Time", "Premium", "Tuned"], values=[], key="-CREATEVEHICLESTABLE-", expand_x=True, expand_y=True)],
    [sg.Text("Total price: 0$\nTotal time: 0 hours", key="-TOTALPRICETIMETEXT-")],
    [sg.Col(expand_y=True, layout=[[]])],
    [cvCreateButton]
]

cvTab = sg.Tab("Create Vehicles",createVehiclesLayout)

#Main graphics
tabGroup = sg.TabGroup([[gplTab,cvTab]],size=(1000,800))

mainLayout = [
    [tabGroup]
]
window = sg.Window(title="Factory Optimizator",layout=mainLayout, size=(1000,600))

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "-GENPRODLOTBUTTON-":
        LOT, LOT_SUMMARY = generateLot()
        lotSummaryTableValues = []
        for vehicleType, vehicles in LOT_SUMMARY.items():
            lotSummaryTableValues.append([ vehicleType,len(vehicles),
                                          len(list(filter(lambda vehicle: vehicle.isPremium, vehicles))), len(list(filter(lambda vehicle: vehicle.isTuned, vehicles))) ])
        window["-LOTSUM-"].update(values=lotSummaryTableValues)
    if event == "-CREATEVEHICLESBUTTON-":
        vehicles = createVehicles(LOT)
        createVehiclesTableValues = []
        totalPrice = 0
        totalTime = 0
        for v in vehicles:
            createVehiclesTableValues.append([v.vin,v.productionPrice,v.hp,v.capacity,v.productionTime,v.isPremium,v.isTuned])
            totalPrice += v.productionPrice
            totalTime += v.productionTime
        window["-CREATEVEHICLESTABLE-"].update(values=createVehiclesTableValues)
        window["-TOTALPRICETIMETEXT-"].update("Total price: " + str(round(totalPrice,2)) + "$\nTotal time: " + str(totalTime) + " hours")
