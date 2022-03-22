from flask import Flask
import xmltodict

app = Flask(__name__)

iss_epoch_data = {}
iss_sighting_data = {}

@app.route('/help', methods=['GET'])
def interaction_info():
    ans = 'To interact with this application, the user must first load in the data by typing "curl -X POST localhost:5035/read_data", this will provide the location and sighting data of the ISS.\nAfter doing so, the user can interact with the application by typing "curl localhost:5035/{command}", where {command} is replaced according to the information desired. Such commands include: /Epochs, /Epochs/<epoch_num>, /Countries, /Countries/<country>, /Countries/<country>/regions,/Countries/regions/<region>, /Countries/<country>/regions/<region>/cities, /Countries/regions/cities/<city> \n'
    return ans

@app.route('/read_data', methods=['POST'])
def read_data_from_file_into_dict():

    global iss_epoch_data
    global iss_sighting_data

    with open( 'ISS.OEM_J2K_EPH.xml', 'r') as f:
        iss_epoch_data = xmltodict.parse(f.read()) 

    with open( 'XMLsightingData_citiesINT03.xml', 'r') as f:
        iss_sighting_data = xmltodict.parse(f.read())

    return f'Data has been read from file\n'

@app.route('/Epochs', methods=['GET'])
def print_epochs():
    for item in iss_epoch_data[data][stateVector]:
        print(item[EPOCH])
    return f'Epochs have been displayed\n'    

@app.route('/Epochs/<epoch_num>', methods=['GET'])
def epoch_data():
    for item in iss_epoch_data[data][stateVector]:
        if item[EPOCH] == epoch_num:
            print(item)
    return f'Epoch data has been displayed\n'

@app.route('/Countries', methods=['GET'])
def print_countries():
    for item in iss_sighting_data[visible_pass]:
        print(item[country])
    return f'Countries have been displayed\n'

@app.route('/Countries/<country>', methods=['GET'])
def country_info():
    for item in iss_sighting_data[visible_pass]:
        if item[country] == country:
            print(item)
    return f'Country information has been displayed\n'

@app.route('/Countries/<country>/regions', methods=['GET'])
def country_regions():
    for item in iss_sighting_data[visible_pass]:
        if item[country] == country:
            print(item[region])
    return f'The regions of the country have been displayed\n'

@app.route('/Countries/regions/<region>', methods=['GET'])
def region_info():
    for item in iss_sighting_data[visible_pass]:
        if item[region] == region:
            print(item)
    return f'Region information has been displayed'

@app.route('Countries/<country>/regions/<region>/cities', methods=['GET'])
def country_and_region_cities():
    for item in iss_sighting_data[visible_pass]:
        if item[country] == country:
            if item[region] == region:
                print(item[city])
    return f'All cities associated with a given country and region have been displayed\n'

@app.route('/Countries/regions/cities/<city>', methods=['GET'])
def city_info():
    for item in iss_sighting_data[visible_pass]:
        if item[city] == city:
            print(item)
    return f'City information has been displayed'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
