# Pycharm Docker compose demo project

Minimal project to reproduce a failure to run skeleton generator. 

## The problem

When opening this project, after having configured Docker as remote interpreter, I'm getting:

```
failed to run generator3/__main__.py for docker-compose://[/Users/bruno/Documents/Workspace/throw-away/pycharm-compose-refresh-bug/docker-compose.yml]:app/python, exit code 2, stderr: ----- python: can't open file '/Users/bruno/Applications/PyCharm Professional Edition.app/Contents/plugins/python/helpers/generator3/__main__.py': [Errno 2] No such file or directory -----
```

Versions:

- macOS Sonoma 14.5
- Pycharm 2024.1.4 Build #PY-241.18034.82, built on June 24, 2024
- Docker Desktop 4.32.0 (157355)
  - Engine: 27.0.3
  - Compose: v2.28.1-desktop.1
  - Credential Helper: v0.8.2
  - Kubernetes: v1.29.2

 ## Solution

 Turn `python.use.targets.api` on.

 1. Open the registry: `Cmd` + `opt` + `shift` + `/`, select registry
 2. Tick the `python.targets.api` checkbox
 3. Restart the IDE
