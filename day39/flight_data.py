class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self,origin_city,price,origin_aiport,destination_city,destination_airport,out_date,return_date,**kwargs):
        self.price = price
        self.origin_city = origin_city
        self.origin_aiport = origin_aiport
        self.destination_city = destination_city
        self.destination_aiport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stop_overs = 0
        self.via_city = ""
        
        