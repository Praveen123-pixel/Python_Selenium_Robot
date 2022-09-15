*** Settings ***
Library     utilities.config.Test_Config
Library     TestKeyword.features.Test_Feature
Test Setup     Launch the Application
Test Teardown  close the application


*** Variables ***


*** Test Cases ***
#TC
Verify the ACTI_time features option's details