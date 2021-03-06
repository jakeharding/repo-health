#Repo Retrieve

Repos are retrieved using the owner's login and the repo's name and a GET request to the url.

URL:
 - `/api/v1/gh-projects?owner__login=<login>&name=<name>`

 Reponse will be a 404 if no project is found.

 Response:
 ```
{
    "id": int,
    "name": str,
    "description": str,
    "language": str,
    "created_at": date str,
    "ext_ref_id": str,
    "deleted": int,
    "owner": int,
    "forked_from": null or int,    
    "contribs_count": int,
    "watchers_count": int,
    "maintainers_count": int,
    "milestones_count": int,
    "orgs_of_contribs_count": int,
    "labels_count": int,
    "commits_count": int,
    "milestones_count": int,
    "owned_by_org": bool,
    "forks_count": int
}
 ```
 
 ## Future Metric possibilities

- maintainers count per month for past year to track project growth
- org members per month over past year to track org growth
