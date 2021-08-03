# import required modules
import requests
# function to request for data
def weather_data(query):
   #API key for my account
   api_key = "5ce0889100cc2d670d70ae1563330715"
   # base url variable to store url
   base_url = "http://api.openweathermap.org/data/2.5/weather?"
   complete_url = base_url + "appid=" + api_key + "&" + query
   # response object
   res=requests.get(complete_url);
   return res.json();
# function used to display results
def display_results(weathers,city):
   print("{}'s temperature: {}°C ".format(city,weathers['main']['temp']))
   print("Wind speed: {} m/s".format(weathers['wind']['speed']))
   print("Description: {}".format(weathers['weather'][0]['description']))
   print("Weather: {}".format(weathers['weather'][0]['main']))
# main function of program
def main():
   # prompt to enter the name of the city 
   city=input('Enter the city:')
   print()
   # try-except block
   try:
      query='q='+city;
      w_data=weather_data(query);
      display_results(w_data, city) #results displayed here 
      print() 
   except:
      print('City name not found')
      
if __name__=='__main__':
   main()