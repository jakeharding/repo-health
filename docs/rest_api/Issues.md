# Issue stats for a repo

Issue stats are retrieved with the repo id.  A GET request is made to the following repo.

 - `/api/v1/gh-projects/<repo-id>/issues`
 
 ```
issues_opened_past_yr: [int], //Issues opened per month over past year from most recent issue
issues_closed_past_yr: [int], //Issues closed per month over past year from most recent issue
issues_count: int,
merged_count: int,
avg_lifetime: str,
popular_labels: [ //Five most popular labels
    label_name: {
        total: int, //total issues with label
        open: int //open issues with label
    }, ...
contrib_comments_per_issue: int
]


```