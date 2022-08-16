from datetime import datetime, timedelta, date
import random as rd
import pandas as pd
import misc as m

#print("Preparing data.........................")

#-------------------------------Customer_ID -------------------------------------
temp_ID = 101
Customer_ID = []

for element in range(195132):
    x = temp_ID
    Customer_ID.append(x)
    temp_ID = temp_ID + 1

rd.shuffle(Customer_ID)
#print("number of customer ID : "+ str(len(Customer_ID)))

#-------------------------------Order_ID -------------------------------------
temp_ID = 15678989
Order_ID = []

for element in range(195132):
    x = temp_ID
    Order_ID.append(x)
    temp_ID = temp_ID + 1
    
rd.shuffle(Order_ID)
#print("number of Order ID : "+ str(len(Order_ID)))


#-------------------------------ProductID -------------------------------------
temp_PID = ['7826','7869','6154']


def PIDGenerator(class1,class2,class3):
    class1_count = int(195132*class1)
    class2_count = int(195132*class2)
    class3_count = int(195132*class3)

    class1_list = []
    class2_list = []
    class3_list = []
    
    for element in range(class1_count):
        temp = temp_PID[0]
        class1_list.append(temp)

    for element in range(class2_count):
        temp = temp_PID[1]
        class2_list.append(temp)

    for element in range(class3_count+2):
        temp = temp_PID[2]
        class3_list.append(temp)

    

    final_list = class1_list + class2_list + class3_list
    #rd.shuffle(final_list)
    return final_list


"""-----Tweak your Qty class percentage here--- |||
                                                vvv  
"""
Product_ID = PIDGenerator(0.53,0.23,0.24)
#print("number of Product ID: " + str(len(Product_ID)))

#-------------------------------Quantity -------------------------------------
temp_Qty = ['1','2']

def QtyGenerator(class1,class2):
    class1_count = int(195132*class1)
    class2_count = int(195132*class2)

    class1_list = []
    class2_list = []
    
    for element in range(class1_count):
        temp = temp_Qty[0]
        class1_list.append(temp)

    for element in range(class2_count):
        temp = temp_Qty[1]
        class2_list.append(temp)

    final_list = class1_list + class2_list
    rd.shuffle(final_list)
    return final_list


"""-----Tweak your Qty class percentage here--- |||
                                                vvv  
"""
Quantity = QtyGenerator(1.0,0.00)
rd.shuffle(Quantity)
#print("number of Quantity: " + str(len(Quantity)))

#-------------------------------Location -------------------------------------
Top10_location_dict = m.get_location_dict()
Location = []

def LocGenerator(loc,percnt):
    class_count = int(1951.32*percnt)

    class_list = []

    for element in range(class_count):
        class_list.append(loc)

    return class_list

for loc,percnt in Top10_location_dict.items():
    temp = LocGenerator(loc,percnt)
    Location.extend(temp)

Others = 195132-len(Location)

for element in range(Others):
    temp = rd.choice(m.Others)
    Location.extend([temp])

rd.shuffle(Location)
#print("number of Location : " + str(len(Location)))

#-------------------------------Date -------------------------------------


length_of_Nothing = Product_ID.count('7826')
Nothing_dates = []

for tareek,percnt in m.Nothing_1stWeek.items():
  temp = m.dateGenerator(length_of_Nothing,tareek,percnt)
  Nothing_dates.extend(temp)

Nothing_others = length_of_Nothing - len(Nothing_dates)

for element in range(Nothing_others):
    temp = rd.choice(m.Nothing_other_dates)
    Nothing_dates.append(temp)
    
#print("Length of Nothing phone dates after others is: ", len(Nothing_dates))



length_of_Oppo = Product_ID.count('7869')
Oppo_dates = []

for tareek,percnt in m.Oppo_1stWeek.items():
  temp2 = m.dateGenerator(length_of_Oppo,tareek,percnt)
  Oppo_dates.extend(temp2)

Oppo_others = length_of_Oppo - len(Oppo_dates)

for element in range(Oppo_others):
    temp = rd.choice(m.Oppo_other_dates)
    Oppo_dates.append(temp)
    
#print("Length of Oppo phone dates is: ", len(Oppo_dates))





length_of_Poco = Product_ID.count('6154')
Poco_dates = []

for tareek,percnt in m.PocoF4_1stWeek.items():
  temp2 = m.dateGenerator(length_of_Poco,tareek,percnt)
  Poco_dates.extend(temp2)

Poco_others = length_of_Poco - len(Poco_dates)

for element in range(Poco_others):
    temp = rd.choice(m.Poco_other_dates)
    Poco_dates.append(temp)
    
#print("Length of Poco phone dates is: ", len(Poco_dates))


Dates = Nothing_dates + Oppo_dates + Poco_dates
#print("number of dates is: ", len(Dates))

  
#-------------------------------List to table - csv -------------------------------------

table = {'Customer_ID' : Customer_ID,
         'Product ID': Product_ID,
         'Quantity' : Quantity,
         'Location' : Location,
         'Date': Dates
    }

def get_order_details():
    dummy_order_data = pd.DataFrame(table)
    return dummy_order_data


dummy_order_data = pd.DataFrame(table)
print("creatig file now.....")

dummy_order_data.to_csv('OrderDetails.csv',index = False)

print("File Created\nCheck in root folder.")



 


    
