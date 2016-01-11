'''
Created on Jan 10, 2016

@author: SG0946321
'''
from com.sabre.api.des.workflow.Activity import Activity
from com.sabre.api.des.rest.activities.InstaFlightActivity import InstaFlightActivity
from com.sabre.api.des.rest.BaseRestCall import BaseRestGetCall
import com.sabre.api.des.config.Configuration as conf

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
        response = BaseRestGetCall(config.getProperty("endpoint") + "/v2/shop/flights/fares", requestObject).executeCall() 
        sharedContext.leadPriceCalendarResult = response
        return InstaFlightActivity()