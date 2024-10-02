docker build -t my-python-app docker
docker run -v /workspaces/my-codespace/ai:/workspaces/my-codespace/ai -it --rm my-python-app /bin/bash 
export OPENAI_API_KEY=""