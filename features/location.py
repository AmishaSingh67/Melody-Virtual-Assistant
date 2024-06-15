import requests

def find_location():
    # Get the public IP address using ipify API
    ip_add = requests.get("https://api.ipify.org").text

    # Construct URL for obtaining geographic information based on the IP address
    url = f"https://get.geojs.io/v1/ip/geo/{ip_add}.json"
    print(url)  # Print constructed URL for debugging

    # Send a GET request to geojs.io API to get geographic information
    geo = requests.get(url)

    # Print the obtained geographic information
    print(geo.text)

    # Extract relevant information from the response
    geo_data = geo.json()
    city = geo_data['city']
    country = geo_data['country']
    state = geo_data['region']
    latitude = geo_data['latitude']
    longitude = geo_data['longitude']
    timezone = geo_data['timezone']
    internet = geo_data['organization']

    # Print the extracted information in a formatted manner
    print(f"City: {city}\nState: {state}\nCountry: {country}\nLatitude: {latitude}\nLongitude: {longitude}\nTimezone: {timezone}\nInternet: {internet}")

    # Return a formatted string containing the geographic information
    return f"City: {city}\nState: {state}\nCountry: {country}\nLatitude: {latitude}\nLongitude: {longitude}\nTimezone: {timezone}\nInternet: {internet}"

# Example usage

#find_location()

