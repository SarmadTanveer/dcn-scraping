# DCN Scraping 
A webscarping and data collection tool to gain some insight into the number and types of public projects awarded to construction companies around Toronto. 

## Inspiration
I have a civil engineer friend who, some time ago, was working as a project estimator at a well known construction company in Toronto. One day we get to talking and he tells me that his company has someone who spends hours browsing the Daily Commercial News website in search of job certificates awarded to their competitors. They then spend more time manually entering this data and creating spreadsheets. This irked me, as I have a firm belief that people should be performing meaningful work not mundane tasks. So I set out to create a tool that will reduce the time to collect this information from weeks to a couple of minutes. Thus the idea was born. 

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
While I didn't gain any monetary value from this, it was good exercise in web scraping and converting data to multiple formats as well as automating a very labour intensive task. Also had the added benefit of making my friend look good. You can check out the retrieved data in the data folder in this repo and as always code suggestions and crticisms are welcomed. 
