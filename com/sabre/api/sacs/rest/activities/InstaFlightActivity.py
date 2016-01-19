'''
Created on Jan 10, 2016

@author: SG0946321
'''
from com.sabre.api.sacs.workflow.Activity import Activity
from com.sabre.api.sacs.rest.activities.BargainFinderMaxActivity import BargainFinderMaxActivity
from com.sabre.api.sacs.rest.BaseRestCall import BaseRestGetCall
import json

class InstaFlightActivity(Activity):
    
    def runActivity(self, sharedContext):
        print("InstaFlightActivity")
        result = json.loads(sharedContext.leadPriceCalendarResult.text)
        url = result['FareInfo'][0]['Links'][0]['href']
        response = BaseRestGetCall(url, None).executeCall()
        sharedContext.instaFlightResult = response
        return BargainFinderMaxActivity()