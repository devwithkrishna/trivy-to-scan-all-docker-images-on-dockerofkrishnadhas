# trivy-to-scan-all-docker-images-on-dockerofkrishnadhas
trivy to scan for vulnerabilities on all docker images in dockerofkrishnadhas dockerhub account

# How code works

* Uses Python language
* using the api end points :
  * https://hub.docker.com/v2/repositories/{account_name}/ --> lists the images under specific dockerhub account.
  * https://hub.docker.com/v2/namespaces/{account_name}/repositories/{image}/tags --> lists image tags under a specific image

* Later uses github workflow to pull the image from dockerhub registry and scan using trivy.

### Dependabot is in Guard

dependabot checks for package updates on `weekly` basis on `every saturday` at `9.00` `Asia/kolkata timezone`

```
The Github workflow is set as cron set to run every week (weekly once) and can be triggered manually at any time.   
workflow file : scan-docker-images-using-trivy.yaml         
```

```
The Github workflow is set as manual and can be triggered any time.   
workflow file : scan-specific-docker-image-using-trivy.yaml         
```


**The dockerhub registry `dockerofkrishnadhas` is a public one.**
***While using private registry authentication needs to be performed.***