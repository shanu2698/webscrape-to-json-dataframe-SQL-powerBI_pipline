import pandas as pd
import random as rd
import json

#print("Preparaing data.....")

#-------------------------------Customer_ID -------------------------------------
temp_ID = 101
Customer_ID = []

for element in range(195132):
    x = temp_ID
    Customer_ID.append(x)
    temp_ID = temp_ID + 1

rd.shuffle(Customer_ID)
#print("number of customer ID : "+ str(len(Customer_ID)))

#-------------------------------Customer_Name -------------------------------------
df = pd.read_csv(r"names.csv")
temp_Name = df['Customer Name'].to_list()
Customer_Name = []

for i in range(195132):# 5200 since the given gap of availability and requirements
    Customer_Name.append(rd.choice(temp_Name))
    
#print("number of Customer Name : "+ str(len(Customer_Name)))

#-------------------------------Customer_Age -------------------------------------

temp_Age14_24 = []
for element in range(14,25):
    temp_Age14_24.append(element)


temp_Age25_45 = []
for element in range(25,46):
    temp_Age25_45.append(element)


temp_Age46_60 = []
for element in range(46,60):
    temp_Age46_60.append(element)

#print(temp_Age14_24)
#print(temp_Age25_45)
#print(temp_Age46_60)


def AgeGenerator(class1,class2,class3):
    class1_count = int(195132*class1)
    class2_count = int(195132*class2)
    class3_count = int(195132*class3)

    class1_list = []
    class2_list = []
    class3_list = []
    
    for element in range(class1_count):
        temp = rd.choice(temp_Age14_24)
        class1_list.append(temp)

    for element in range(class2_count):
        temp = rd.choice(temp_Age25_45)
        class2_list.append(temp)

    for element in range(class3_count+1):
        temp = rd.choice(temp_Age46_60)
        class3_list.append(temp)


    final_list = class1_list + class2_list + class3_list
    rd.shuffle(final_list)
    return final_list


"""-----Tweak your Age class percentage here--- |||
                                                vvv  
"""
Customer_Age = AgeGenerator(0.6,0.25,0.15) 
#print("number of Customer Age : " + str(len(Customer_Age)))

#-------------------------------Customer_Sex -------------------------------------

temp_sex = ['Male','Female','Others']


def Sex_Generator(class1,class2,class3):
    class1_count = int(195132*class1)
    class2_count = int(195132*class2)
    class3_count = int(195132*class3)

    class1_list = []
    class2_list = []
    class3_list = []

    for element in range(class1_count):
        temp = temp_sex[0]
        class1_list.append(temp)

    for element in range(class2_count):
        temp = temp_sex[1]
        class2_list.append(temp)

    for element in range(class3_count+1):
        temp = temp_sex[2]
        class3_list.append(temp)


    final_list = class1_list + class2_list + class3_list
    rd.shuffle(final_list)
    return final_list


Customer_Sex = Sex_Generator(0.6,0.35,0.05) #<<-----Tweak your sex class percentage here-----
#print("number of Customer Sex : " + str(len(Customer_Sex)))


#-------------------------------Customer_PaymentMode -------------------------------------



temp_PayMode = ['Credit Card','Debit Card','Cash on Delivery']


def PayMode_Generator(class1,class2,class3):
    class1_count = int(195132*class1)
    class2_count = int(195132*class2)
    class3_count = int(195132*class3)

    class1_list = []
    class2_list = []
    class3_list = []

    for element in range(class1_count):
        temp = temp_PayMode[0]
        class1_list.append(temp)

    for element in range(class2_count):
        temp = temp_PayMode[1]
        class2_list.append(temp)

    for element in range(class3_count+1):
        temp = temp_PayMode[2]
        class3_list.append(temp)


    final_list = class1_list + class2_list + class3_list
    rd.shuffle(final_list)
    return final_list


Customer_PayMode = PayMode_Generator(0.6,0.20,0.20) #<<-----Tweak your PayMode class percentage here-----
#print("number of Customer PayMode : " + str(len(Customer_PayMode)))

#-------------------------------List to table - csv -------------------------------------

table = {'Customer_ID' : Customer_ID,
         'Customer_Name': Customer_Name,
         'Customer_Age' : Customer_Age,
         'Customer_Sex' : Customer_Sex,
         'Customer_PayMode': Customer_PayMode
    }


def get_customer_details():
    dummy_customer_data = pd.DataFrame(table)
    return dummy_customer_data


"""
dummy_customer_data = pd.DataFrame(table)

print("creatig file now.....")

dummy_customer_data.to_csv('CustomerData.csv',index = False)

print("File Created\nCheck in root folder.")
"""
