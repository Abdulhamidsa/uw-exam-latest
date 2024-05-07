from bottle import get, template, static_file
import x
from icecream import ic
import requests
 
##############################
@get("/")
def _():
  ic("xxxxxxx")
  return "5555"
 


@get("/")
def _():
  ic("xxxxxxx")
  return "5555"

@get("/get-crimes")
def _():
    response = requests.get("https://abdulhamidsa.pythonanywhere.com/crimes")
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract JSON data from the response
        crimes_data = response.json()
        
        # Iterate over each crime in the fetched data
        for crime in crimes_data:
            # Insert the crime into the crimes collection
            query = {
                "query": """
                    INSERT @crime INTO crimes RETURN NEW
                """,
                "bindVars": {
                    "crime": crime
                }
            }
            res = x.db(query)
            ic(res)

        # Return a success message
        return "JSON data fetched and inserted into the crimes collection"
    else:
        # Log an error if the request was not successful
        ic("Error fetching JSON data. Status code:", response.status_code)
        return "Error fetching JSON data"
##############################
# @get("/get-crimes")
# def _():
#   # Make a GET request to fetch data from the external API
#   response = requests.get("https://abdulhamidsa.pythonanywhere.com/crimes")
  
#   # Check if the request was successful (status code 200)
#   if response.status_code == 200:
#     # Extract and log the JSON data
#     crimes_data = response.json()
#     ic(crimes_data)
    
#     # Return a success message
#     return "JSON data fetched and logged in the console"
#   else:
#     # Log an error if the request was not successful
#     ic("Error fetching JSON data. Status code:", response.status_code)
#     return "Error fetching JSON data"


  # Extract the suspects from the crime
  # The crime will be the same without suspect
 
  # suspects = crime["suspects"]
  # ic("#"*30)
  # ic(suspects)
 
 
  # Save the crime to the crimes collection, make sure
  # that you get back the crime's id: Eg: crimes/4565656
 
 
  # query = {
  #   "query": """
  #     INSERT @crime INTO crimes RETURN NEW
  #   """,
  #   "bindVars": {
  #     "crime": crime
  #   }
  # }
  # res = x.db(query)
  # ic(res)
 
  # # Get the id of the crime
  # crime_id = res["result"][0]["_id"]
  # ic(crime_id)
  # # res->result->0->_id
  # # return "crimes saved in arangodb"
 
 
  # query = {
  #   "query": """
  #     INSERT @suspect INTO suspects RETURN NEW
  #   """,
  #   "bindVars": {
  #     "suspect": suspects[0]
  #   }
  # }
  # res = x.db(query)
  # suspects_id = res["result"][0]["_id"]
  # ic(suspects_id)
 
  # # Gold Challenge
  # # Insert the crime and the suspect in the edge collection
 
  # doc = {"_from":crime_id, "_to":suspects_id}
  # query = {
  #   "query": """
  #     INSERT @doc INTO crimes_commited_by_suspects RETURN NEW
  #   """,
  #   "bindVars": {
  #     "doc": doc
  #   }
  # }
  # x.db(query)
 
  # return "crimes and suspects saved in arangodb"