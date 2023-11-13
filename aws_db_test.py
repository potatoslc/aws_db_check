#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 09:50:03 2023

@author: potato
"""
import mysql.connector
import pymysql
import sys
import boto3
import os

# Replace with your RDS endpoint and database credentials
endpoint = "database-1.czikup7sd3q9.us-east-2.rds.amazonaws.com"
username = "admin_test"
password = "admintest"
database_name = "database-1"
region = "us-east-2a"
port = "1433"

#method1
def method1():
        
    connection = mysql.connector.connect(
        host=endpoint,
        user=username,
        password=password,
        database=database_name
    )
    
    if connection.is_connected():
        print("Connected to MySQL database")
        cursor = connection.cursor()
    
        # Example SQL command
        sql_query = """create table logintest (
        date varchar(256),
        time varchar(256),
        user varchar(256)
        );"""
        cursor.execute(sql_query)
    
        # Fetch and print the results
        results = cursor.fetchall()
        for row in results:
            print(row)
    
        cursor.close()
    
    else:
        print("Connection failed")
    
    # Close the connection when you're done
    connection.close()

#method2
os.environ['LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN'] = '1'
session = boto3.Session(profile_name='default')
client = session.client('rds')

token = client.generate_db_auth_token(DBHostname=endpoint, Port=port, DBUsername=username, Region=region)

try:
    conn =  pymysql.connect(host=endpoint, user=username, passwd=token, port=port, database=database_name, ssl_ca='SSLCERTIFICATE')
    cur = conn.cursor()
    cur.execute("""SELECT now()""")
    query_results = cur.fetchall()
    print(query_results)
except Exception as e:
    print("Database connection failed due to {}".format(e))  
    
    

from datetime import date,datetime    
import pymysql
def record_login(role:str):
    
    curr_time = datetime.now()
    curr_time_fm = curr_time.strftime("%H:%m")
    today_date = date.today()
    connection = pymysql.connect(host='database-2.czikup7sd3q9.us-east-2.rds.amazonaws.com',
                             user='admin',
                             password='admintest',
                             database='',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    cursor.execute("use login_db")
    curr_query = "insert into login values ( '"+str(today_date) +"','"+ str(curr_time) +"','"+role+ "')"
    
    try:
        cursor.execute(curr_query)
        cursor.execute("select * from login")
        result1 = cursor.fetchall()
        for row in result1:
            print(row)
        print("Query run succeed")
    except Exception as error:
        print("There is exception happened:", type(error).__name__,"-",error)
        
    
    
    

import pymysql
import requests
def record_login(role:str):
    url = "https://worldtimeapi.org/api/timezone/America/Denver"
    response = requests.get(url)
    result = response.json()
    date_in = result["datetime"]
    date = date_in[0:10]
    time = date_in[11:19]
  

    connection = pymysql.connect(host='database-2.czikup7sd3q9.us-east-2.rds.amazonaws.com',
                             user='admin',
                             password='admintest',
                             database='login_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    #cursor.execute("use login_db;")
    curr_query = "insert into login values ( '"+str(date) +"','"+ str(time) +"','"+role+ "')"

    try:
        cursor.execute(curr_query)
        connection.commit()
        """
        cursor.execute("select * from login_n;")
        result1 = cursor.fetchall()
        for row in result1:
            print(row)
        #print("Query run succeed")
        """
    except Exception as error:
        print("There is exception happened:", type(error).__name__,"-",error)

    cursor.close()
    return 


def read_record():
    url = "https://worldtimeapi.org/api/timezone/America/Denver"
    response = requests.get(url)
    result = response.json()
    date_in = result["datetime"]
    date = date_in[0:10]
    time = date_in[11:19]
  

    connection = pymysql.connect(host='database-2.czikup7sd3q9.us-east-2.rds.amazonaws.com',
                             user='admin',
                             password='admintest',
                             database='login_db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = connection.cursor()
    #cursor.execute("use login_db;")

    try:
        cursor.execute("select * from login_n")
        result1 = cursor.fetchall()
        for row in result1:
            print(row)
        #connection.commit()
        """
        cursor.execute("select * from login_n;")
        result1 = cursor.fetchall()
        for row in result1:
            print(row)
        #print("Query run succeed")
        """
    except Exception as error:
        print("There is exception happened:", type(error).__name__,"-",error)

    cursor.close()
    return 





