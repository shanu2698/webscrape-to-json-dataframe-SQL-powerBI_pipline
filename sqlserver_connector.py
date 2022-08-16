# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 17:01:50 2022

@author: WIIS
"""

import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=EXR03-TEMP;'
                      'Database=Power_BI;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
"""
cursor.execute('''
		CREATE TABLE prods (
			product_id int primary key,
			product_name nvarchar(50),
			price int
			)
               ''')
"""
cursor.execute('''
		INSERT INTO prods (product_id, product_name, price)
		VALUES
			(11,'Desktop Computer',1500),
			(12,'Laptop',1800),
			(13,'Tablet',900),
			(14,'Monitor',850),
			(15,'Printer',950)
                ''')
conn.commit()
print("Command sent s")
