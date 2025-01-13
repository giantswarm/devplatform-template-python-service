# devplatform-template-go-service

This project is a template project to bootstrap golang repositories using the Giant IDP.
Please read the notes below to understand how this repository works and is kept up to date.

## Updating the template

If you want to update any files that are templated when a new project is created, you should
create a new topic branch and then a new PR from that branch against the `main` branch.
For each PR, a separate github action is run to create a preview PR with the changes applied (a sub-PR).
That sub-PR runs the templating logic against your topic branch and then compares the rendered result with
the current status of the `rendered-project` branch. For the sub-PR, all tests are invoked and their status is reported in the sub-PR. The original PR will have a link to the sub-PR, so you can check its status. The original
PR will be also blocked with status checks until the sub-PR is merged.
Once you're happy with the change in the sub-PR, you should merge it (the changes will go to `rendered-project`
branch). Once that's done, you can merge the original PR as well.

> [!WARNING]
> Currently, the status of the sub-PR is not automatically refelcted in the main PR. After you merge the sub-PR, you have to
> manually trigger a re-run of the "check if sub-PR is merged" check.

### Renovate

Renovate correctly detects dependencies and creates PR against the `main` branch.

### Example

1. A topic branch and a PR created by renovate to update a github action in the `project-template`` directory
   <https://github.com/giantswarm/devplatform-template-go-service/pull/118/files>

2. A comment in the PR to the templated sub-PR and its check result
   <https://github.com/giantswarm/devplatform-template-go-service/pull/118#issuecomment-2580213836>

```
Comment on #118 chore(deps): update sigstore/cosign-installer action to v3.7.0
Pull request #136 was created to preview the result of this PR.
Make sure you review and accept the created PR before you merge this one here.
<https://github.com/giantswarm/devplatform-template-go-service|giantswarm/devplatform-template-go-service>giantswarm/devplatform-template-go-service | Today at 2:45 PM | Added by GitHub
```

3. The templated sub-PR itself
   <https://github.com/giantswarm/devplatform-template-go-service/pull/136>
