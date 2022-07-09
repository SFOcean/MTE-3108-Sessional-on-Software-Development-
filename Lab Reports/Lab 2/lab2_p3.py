import datetime

class NewsStory:
    guid = str()
    title = str()
    description = str()
    link = str()
     
    # parameterized constructor
    def __init__(self, g, t, d, l):
        self.guid = g
        self.title = t
        self.description = d
        self.link = l

     
    def get_guid(self):
        print("Globally Unique Identifier (GUID) - " + str(self.guid))

    def get_title(self):
        print("Title - " + str(self.title))

    def get_description(self):
        print("Description - " + str(self.description))

    def get_link(self):
        print ("Link - " + str(self.link))


 
# creating object of the class
# this will invoke parameterized constructor

obj = NewsStory("Bangladesh", "Bike Banned In Bangladesh", "All types of bikes are banned in bangladesh in eid", "Link1")
 
# perform Addition
obj.get_title()
 
# display result
obj.get_link()