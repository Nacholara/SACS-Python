'''
Created on Jan 25, 2016

@author: SG0946321
'''
from com.sabre.api.sacs.workflow.Activity import Activity
from com.sabre.api.sacs.rest.BaseRestCall import BaseRestGetCall
import com.sabre.api.sacs.config.Configuration as conf
import json

class MCT(Activity):
    
    def runActivity(self, sharedContext):
        print("MCT")
        config = conf.Configuration()
        # result = json.loads(sharedContext.leadPriceCalendarResult.text)
        url = config.getProperty('environment') + '/v1.0.0/log/transactions'
        response = BaseRestGetCall(url, None).executeCall()
        sharedContext.instaFlightResult = response
        return None