# Contributing

# git

## branches

We use feature branches. The name of your feature branch should use the following syntax:

`<issue_number>-<description-with-hypens>` i.e. `100-new-xml-feature`

A typical checkout and merge use case looks like the following:

```commandline
(venv) ➜  widow-producer git:(master) %  # Start on master

# Create/Check out feature branch
(venv) ➜  widow-producer git:(master) %  git checkout -b 100-new-feature  

# Commit your changes
(venv) ➜  widow-producer git:(100-new-feature) %  git commit -a -m "feature(*): Added new xml feature"  

# Push your changes (you may need to set up your remote branch)
(venv) ➜  widow-producer git:(100-new-feature) % git push

# Merge 100-new-feature into master on GitLab by opening a merge request
```

## commits

We use `Angular` type messages for commits: https://github.com/angular/angular.js/blob/master/DEVELOPERS.md#type

Types: feat, fix, docs, style, refactor, perf, test, chore

This helps us track commit history and versioning.