# ISS Position and Sightings

## Overview
The following repository contains a containarized Flask app that provides the user with interesting data about the ISS location and sighting. The data utilized to run this application was obtained from the NASA website, and the application allows the user to obtain information of interest without having to navigate through the raw data, making the data more accesible and efficient.

## Files
This repository contains the following files:

### app.py
This python script is utilized to create endpoints that provide the data requested by the user. It utilizes Flask as the API used to create the application

### pytest_app.py
This python script tests the functions found the in the app.py script. It ensures that the defined functions return the correct output and provide the desired data.

### Dockerfile
This file was utilized to create a contained in Docker Hub using the files in the current repository

### Makefile
This file was utilized to automate testing for the service of the application

## Download Original Data
The original data can be downlaoded in the following link:
https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq
The files used for this application were: Public Distribution File and XMLsightingData_citiesINT03

## Curl
To navigate the application, the user can learn to do so by typing "curl localhost:5035/Help". This will provide information on how to run the application an what information it can provide

## Citations
The data utilized in this project was obtained from the NASA website, found in the following link: https://data.nasa.gov/Space-Science/ISS_COORDS_2022-02-13/r6u8-bhhq

