#Pull requests stats for  a repo

Pull request stats are retrieved with the repo id. `prs` is used as an abbreviation for pull requests.
A GET request is made to:
- `/api/v1/gh-projects/<repo-id>/pull-requests`
- Note the repo id embedded in the URL


```
{
    "prs_count": int,
    "prs_last_year:  [int] //12 element array, number of prs per month,oldest first, one year from latest_pr_created_at
    "latest_pr_created_at": datetime str,
    "contrib_most_prs": str - login,
    "prs_no_maintainer_comments": int,
    "prs_no_comments": int,
    "avg_lifetime": str,
    "not_maintainer_prs": int,
    "avg_comment_per_pr": float,
    "prs_from_outside_org": int
}
```