'''
Created on Nov 27, 2015

@author: SG0946321
'''
from com.sabre.api.sacs.rest.activities.LeadPriceCalendarActivity import LeadPriceCalendarActivity
from com.sabre.api.sacs.workflow.Workflow import Workflow
from com.sabre.api.sacs.rest.activities.MCT import MCT

workflow = Workflow(LeadPriceCalendarActivity())
# workflow = Workflow(MCT())
sharedContext = workflow.runWorkflow()
print("---------------------- RESULTS --------------------------")
print(sharedContext.leadPriceCalendarResult.text)
print(sharedContext.instaFlightResult.text)
print(sharedContext.bargainFinderMaxResult.text)