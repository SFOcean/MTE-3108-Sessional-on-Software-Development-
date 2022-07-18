#Importing date class from datetime module
from datetime import date

class NewsStory: 
    # parameterized constructor
    def __init__(self, g, t, d, l):
        self.guid = g
        self.title = t
        self.description = d
        self.link = l
        self.dateTime = date.today()
    #Creating Methods
    def get_guid(self):
        print("Globally Unique Identifier (GUID) - " + str(self.guid))
    def get_title(self):
        print("Title - " + str(self.title))
    def get_description(self):
        print("Description - " + str(self.description))
    def get_link(self):
        print ("Link - " + str(self.link))
    def get_update(self):
        print ("Update - " + str(self.dateTime))
 
# creating object of the class
obj = NewsStory("ImWmfG+1g0uDYqb8NWgqrg==", "Bike Banned In Bangladesh", "All types of bikes are banned in bangladesh for eid due to some accidents. Bikers didn't like that.", "https://www.tbsnews.net/bangladesh/now-inter-district-travel-motorcycles-be-banned-7-days-452234")
 
#Calling Methods to print the results
obj.get_guid()
obj.get_title()
obj.get_description()
obj.get_link()
obj.get_update()