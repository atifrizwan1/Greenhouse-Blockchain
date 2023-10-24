
import random

def weights(curr,out,pref):
    w = 1
    if(curr <out and out < pref[0]):
        w = 1/(curr-out)
    elif(out<curr and curr < pref[0]):
        w = 1-(1/(curr-out))
    elif(curr > out and out > pref[1]):
         wT = 1/(curr-out)
    elif(out > curr and curr > pref[1]):
         w = 1-(1/(curr-out))
    else:
        w = 1
    return w
        
def BasicCoolingCost_Rules(currTemp):
    BasicEnergyCost = 0
    # difference 14kW cooling capacity
    if(currTemp <= 16.0 and currTemp >= 15.0):
        BasicEnergyCost = random.uniform(0,1) #1.34 
    elif(currTemp <= 17.0 and currTemp >= 16.0):
        BasicEnergyCost =  random.uniform(0,1) # 1.22
    elif(currTemp <= 18.0 and currTemp >= 17.0):
        BasicEnergyCost =  random.uniform(0,1)#1.08
    elif(currTemp <= 19.0 and currTemp >= 18.0):
        BasicEnergyCost =  random.uniform(0,1)#0.99
    elif(currTemp >= 19.0 and currTemp <= 20.0) :
        BasicEnergyCost =  random.uniform(0,1)#0.97
    elif(currTemp >= 20.0 and currTemp <= 21.0):
        BasicEnergyCost =  random.uniform(0,1)#0.96
    elif(currTemp >= 21.0 and currTemp <= 22.0):
        BasicEnergyCost =  random.uniform(0,1)#0.94
    elif(currTemp >= 22.0 and currTemp <= 23.0):
        BasicEnergyCost =  random.uniform(0,1)#0.91
    elif(currTemp >= 23.0 and currTemp <= 24.0):
        BasicEnergyCost =  random.uniform(0,1)#0.90
    elif(currTemp >= 24.0 and currTemp <= 25.0):
        BasicEnergyCost =  random.uniform(0,1)#0.899
    
    return BasicEnergyCost

#--- Humidity Basic Energy Consumption Rules ------------------------------------------------------------+
def BasicHumidCost_Rules(currHumid):
    BasicEnergyCost = 0
                        # difference 14kW cooling capacity
    if(currHumid < 40.0):
        BasicEnergyCost =  random.uniform(0,2)#0.98
    elif(currHumid <= 45.0 and currHumid >= 40.0):
        BasicEnergyCost =  random.uniform(0,2) #0.99 
    elif(currHumid <= 50.0 and currHumid >= 45.0):
        BasicEnergyCost =  random.uniform(0,2)#1.08
    elif(currHumid <= 55.0 and currHumid >= 50.0):
        BasicEnergyCost =  random.uniform(0,2)#1.22
    elif(currHumid <= 60.0 and currHumid >= 55.0):
        BasicEnergyCost =  random.uniform(0,2)#1.34
    elif(currHumid >= 60.0):
        BasicEnergyCost =  random.uniform(0,2)#1.5
    return BasicEnergyCost

def BasicCO2Cost_Rules(currCO2):
    BasicEnergyCost = 0
    # difference 14kW cooling capacity
    if(currCO2 >= 350.0 and currCO2 <= 400.0):
        BasicEnergyCost =  random.uniform(0,2)#0.98
    elif(currCO2 <= 420.0 and currCO2 >= 400.0):
        BasicEnergyCost =  random.uniform(0,2)#0.99 
    elif(currCO2 <= 430.0 and currCO2 >= 420.0):
        BasicEnergyCost =  random.uniform(0,2)#1.08
    elif(currCO2 <= 450.0 and currCO2 >= 430.0):
        BasicEnergyCost =  random.uniform(0,2)#1.22
    elif(currCO2 <= 470.0 and currCO2 >= 450.0):
        BasicEnergyCost =  random.uniform(0,2)#1.34
    elif(currCO2 >= 470.0 and currCO2 <= 490.0):
        BasicEnergyCost =  random.uniform(0,2)#1.5
    elif(currCO2 >= 490.0 and currCO2 <= 520.0):
        BasicEnergyCost =  random.uniform(0,2)#1.5
    elif(currCO2 >= 520.0 and currCO2 <= 550.0):
        BasicEnergyCost =  random.uniform(0,2)#1.5
    else:
        BasicEnergyCost = random.uniform(0,2) # 1.6
    return BasicEnergyCost


