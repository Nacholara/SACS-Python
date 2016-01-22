'''
Created on Jan 10, 2016

@author: SG0946321
'''
from com.sabre.api.sacs.workflow.Activity import Activity
from com.sabre.api.sacs.rest.activities.InstaFlightActivity import InstaFlightActivity
from com.sabre.api.sacs.rest.BaseRestCall import BaseRestGetCall
import com.sabre.api.sacs.config.Configuration as conf

class LeadPriceCalendarActivity(Activity):
    
    def runActivity(self, sharedContext):
        print("LeadPriceCalendar")
        config = conf.Configuration()
        requestObject = {
            'origin' : 'LAX',
            'destination' : 'JFK',
            'lengthofstay' : 5,
            'pointofsalecountry' : 'US'
        }
        response = BaseRestGetCall(config.getProperty("environment") + "/v2/shop/flights/fares", requestObject).executeCall() 
        sharedContext.leadPriceCalendarResult = response
        return InstaFlightActivity()