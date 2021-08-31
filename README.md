# DCN Scraping 
A webscarping and data collection tool to gain some insight into the number and types of public projects awarded to construction companies around Toronto. 

## Design and Implementation 
The tool itself is broken down into submodules that each perform a single overarching task. For simplicity these submodules are located in the collector package. The task can be broken down into four subtasks (submodules); searching, scraping, save as json, save as excel. 

### Searching: The links module
The functions in this module search the dcn website for all certificates issued under a certain name and then retrieve the urls for each certificate issued under the company name. 

### Scraping: The certParser module
This module provides functions to scrape each of the provided links and retrieve the certificate data in the desired format. 

### Save as json: jsonConv module 
This module provides functions to write data and read data as json. This was done in an effort to build a local database of certificates that would represent the data avaialble on dcn. 

### Save as excel: excel module 
This module creates excel sheets for each individual company and also provides a function to append data to the desired sheet row by row. 

## Result
This was good exercise in web scraping and converting data to multiple formats as well as automating a very labour intensive task. Code suggestions and crticisms are welcomed. 
