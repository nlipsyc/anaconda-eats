# QA Engineer Prompt

## UI Tests 
Write test scenarios for the following use cases

1. Navigate to https://anaconda.cloud
2. Search for “Python” 
3. Validate the results under Content section
4. Validate the the results under Package section

### Automate the above test scenarios

When implementing these automation tests consider different aspects of testing as you would on your day to day work. 

### Consider the following when creating the automation tests  
- Screenshot  in case of failures
- Report of the passed and failed test


## API Tests 
Refer to this API swagger doc `http://anacondaeats.pythonanywhere.com/#/` and write test scenarios for the following use cases considering all the aspects of testing.

1. Send a request to retrieve the existing receipes
2. Add a brand new receipe 
3. Retrieve the newly added receipe
4. Update the receipe that you just added on step 2.
5. Publish the updated receipe
6. Delete the receipe you just added

### Automate the above test scenarios

When implementing these automation tests consider different aspects of testing as you would on your day to day work to test the end point throughly. 

### Consider the following when creating the automation tests  
- Invalid scenarios and what would likely break the APIs or capture the errors.
- Report of the passed and failed test