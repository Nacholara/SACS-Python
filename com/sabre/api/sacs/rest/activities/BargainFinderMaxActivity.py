'''
Created on Jan 10, 2016

@author: SG0946321
'''
from com.sabre.api.sacs.workflow.Activity import Activity
from com.sabre.api.sacs.rest.BaseRestCall import BaseRestPostCall
import com.sabre.api.sacs.config.Configuration as conf

class BargainFinderMaxActivity(Activity):
    
    def runActivity(self, sharedContext):
        print("BargainFinderMax")
        config = conf.Configuration()
        response = BaseRestPostCall(config.getProperty("environment") + "/v1.9.2/shop/flights?mode=live", self.createRequest(sharedContext)).executeCall()
        sharedContext.bargainFinderMaxResult = response
        return None
    
    def createRequest(self, sharedContext):
        return {
            "OTA_AirLowFareSearchRQ": {
                "Target": "Production",
                    "POS": {
                        "Source": [{
                            "RequestorID": {
                                "Type": "1",
                                "ID": "1",
                                "CompanyName": {}
                            }
                        }]
                    },
                    "OriginDestinationInformation": [{
                        "RPH": "1",
                        "DepartureDateTime": sharedContext.departureDate+"T11:00:00",
                        "OriginLocation": {
                            "LocationCode": sharedContext.origin
                        },
                        "DestinationLocation": {
                            "LocationCode": sharedContext.destination
                        },
                        "TPA_Extensions": {
                            "SegmentType": {
                                "Code": "O"
                            }
                        }
                    }],
                    "TravelPreferences": {
                        "ValidInterlineTicket": True,
                        "CabinPref": [{
                            "Cabin": "Y",
                            "PreferLevel": "Preferred"
                        }],
                        "TPA_Extensions": {
                            "TripType": {
                                "Value": "Return"
                            },
                            "LongConnectTime": {
                                "Min": 780,
                                "Max": 1200,
                                "Enable": True
                            },
                            "ExcludeCallDirectCarriers": {
                                "Enabled": True
                            }
                        }
                    },
                    "TravelerInfoSummary": {
                        "SeatsRequested": [1],
                        "AirTravelerAvail": [{
                            "PassengerTypeQuantity": [{
                                "Code": "ADT",
                                "Quantity": 1
                            }]
                        }]
                    },
                    "TPA_Extensions": {
                        "IntelliSellTransaction": {
                            "RequestType": {
                                "Name": "50ITINS"
                            }
                        }
                    }
                }
            }
