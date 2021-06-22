#!/usr/bin/env python
# coding: utf-8

# In[1]:


from simpful import *


# In[2]:


FS = FuzzySystem()


# ## Define fuzzy sets and linguistic variables
# 

# In[3]:


# Passing Variables
P1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=2 , d = 6), term="Low")
P2 = FuzzySet(function=Triangular_MF(a=4, b=8, c=12), term="Medium")
P3 = FuzzySet(function=Trapezoidal_MF(a=10, b=16, c=18 , d = 18), term="High")
FS.add_linguistic_variable("PassingVehicles", LinguisticVariable([P1, P2, P3], universe_of_discourse=[0,18]))


# In[4]:


# Waiting Variables 
W1 = FuzzySet(function=Trapezoidal_MF(a=0, b=0, c=1 ,d = 5), term="Low")
W2 = FuzzySet(function=Triangular_MF(a=3, b=6, c=9), term="Medium")
W3 = FuzzySet(function=Trapezoidal_MF(a=10, b=14, c=15 , d = 15), term="High")
FS.add_linguistic_variable("WaitingVehicles", LinguisticVariable([W1, W2, W3], universe_of_discourse=[0,15]))


# ## Define output fuzzy sets and linguistic variable
# 

# In[5]:


# Define output fuzzy sets and linguistic variable

GLD1 = FuzzySet(function=Triangular_MF(a=0, b=0, c=15), term="Short")
GLD2 = FuzzySet(function=Triangular_MF(a=10, b=16, c=25), term="Medium")
GLD3 = FuzzySet(function=Trapezoidal_MF(a=22, b=35, c=40 , d = 40), term="Long")
FS.add_linguistic_variable("GreenLightDuration", LinguisticVariable([GLD1, GLD2, GLD3], universe_of_discourse=[0,40]))


# ## Define Fuzzy Rules
# 

# In[6]:


#Aggregation for short output
R1 = "IF (WaitingVehicles IS Low) AND (PassingVehicles IS Low) THEN (GreenLightDuration IS Short)"
R2 = "IF (WaitingVehicles IS Medium) AND (PassingVehicles IS Low) THEN (GreenLightDuration IS Short)"
R3 = "IF (WaitingVehicles IS High) AND (PassingVehicles IS Low) THEN (GreenLightDuration IS Short)"
R4 = "IF (WaitingVehicles IS High) AND (PassingVehicles IS Medium) THEN (GreenLightDuration IS Short)"
R5 = "IF (WaitingVehicles IS High) AND (PassingVehicles IS High) THEN (GreenLightDuration IS Short)"

#Aggregation for Medium output
R6 = "IF (WaitingVehicles IS Low) AND (PassingVehicles IS Medium) THEN (GreenLightDuration IS Medium)"
R7 = "IF (WaitingVehicles IS Medium) AND (PassingVehicles IS Medium) THEN (GreenLightDuration IS Medium)"
R8 = "IF (WaitingVehicles IS Medium) AND (PassingVehicles IS High) THEN (GreenLightDuration IS Medium)"

#Aggregation for Long output
R9 = "IF (WaitingVehicles IS Low) AND (PassingVehicles IS High) THEN (GreenLightDuration IS Long)"

FS.add_rules([R1, R2, R3, R4, R5, R6, R7, R8, R9])


# ## Defuzzification

# In[7]:


# Set Input values
FS.set_variable("WaitingVehicles", 3)
FS.set_variable("PassingVehicles", 14)

# Perform Mamdani inference and print output
print(FS.Mamdani_inference(["GreenLightDuration"]))

