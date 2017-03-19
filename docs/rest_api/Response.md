# REST API response schema

Represents a response schema for a request to the API. A list of metrics are returned to allow
 the client to iterate over the response and build the UI based on what the API provides.
 
 Comments are added for clarification.
 
 ```
 [
    {
        display: string, //display name of the metric
        ordering: int, //order if the metric in UI
        metric: int | [int] | string, //Actual data. Array of ints if it is a chart
        chart_type: null | string, //Type of chart if chart is used
        chart_name: null | stirng, //Name of chart to allow multiple metrics on one chart
        
    },
    ...
 ]
 ```
 ## OR
 
```
{
    ...//Maybe some other data defining the Response to the UI
    charts: {
        chart_name : {
            chart_type: int, //Enumerate chart types?
            x_names: [string],
            y_names: [string]
        },
        ...
    },
    metrics: [
        {
            is_displayed: bool,  //Should the metric be displayed in the UI
            display_name: string, //display name of the metric
            ordering: int, //order of the metric in UI. Order of chart is metric is in chart
            metric: int | [int] | string | bool, //Actual data. Array of ints if it is a chart
            chart_name: null | string, //Name of chart to allow multiple metrics on one chart
            
        },
...
    ]
 }
 ```