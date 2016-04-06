# General
## Overview
The Sabre API Code Samples for Python project’s purpose is to provide the reference code and enable quick and easy start to consuming Sabre Webservices. It focuses on business case usage, so it shows how to chain several REST calls into a workflow, where the subsequent call uses the previous one’s result. Its structure is designed to easily reuse parts of the classes, whole classes, modules or even whole project in client’s applications.

## Configuring the application
The configuration is located in *SACSConfig.properties* file. It keeps the properties which are needed to connect and authenticate to the Sabre’s REST webservices. They are being read by the Configuration class, which contains 2 methods:

- *getProperty()* – it reads the value of the property which is not encrypted.
- *getEncryptedProperty()* – reads and decrypts the encrypted property.
Although the credentials are not encrypted right now to lower the project entry time, it is strongly recommended to use the encryption in production systems and do not keep the credentials in plain text.
Please register at https://developer.sabre.com in order to obtain your own credentials.

## Running the application
## Quickstart “How to”
The workflow’s activities are written as subclasses of the Activity class from the *com.sabre.api.sacs.workflow* package, which contains one abstract method *runActivity()* which takes the shared context as the parameter. The implementation should construct the request object (or just setup the URL, like in the *InstaFlight* case), execute a rest call, insert the call’s result into the *sharedContext* and return the next activity to be run.

# Modules
## Configuration
This module provides configuration of REST webservice calls. It contains the endpoint address and credentials to connect there, which are not encrypted. The encryption and decryption methods are included.

## Rest
A set of modules containing classes used to communicate with Sabre’s REST webservices. The *BaseRestCall* contains classes for GET and POST call, which can be used to easily execute REST call. It uses the *TokenHolder* class, which takes care of providing token to authenticate the call, which is obtained by executing the *AuthenticationCall* class' *callForToken()* method.

The main runnable script is also contained there and is named *Rest.py*.

## Activities
The package contains three implementations of the *Activity* class used in the *Workflow* module. The *LeadPriceCalendarActivity* executes the GET call, the *InstaFlightActivity* uses a hypermedia link from the result of the *LeadPriceCalendar* call, and the *BargainFinderMaxActivity* runs a POST call.

## Workflow
Module used to run a sequence of activities. Each activities’ *runActivity()* method returns the next activity to be run, until there is no more.
