# python-template-based-on-docker

FYI: [Dockerコンテナ上で動くPythonの開発環境のテンプレートを作ってみた](https://zenn.dev/fitness_densuke/articles/python_template_based_on_docker)

## Prerequisites

- Tool to run Docker like Docker Desktop
  - I highly recommend to use [OrbStack](https://github.com/orbstack/orbstack)

## Apply template to your project
```
git clone https://github.com/tamtam-fitness/python-template-based-on-docker.git <new-project>

cd <new-project>

rm -rf .git
```

## Run Container

To start development, you are supposed to run the following command:
```bash 
make setup   
```

## Development Commands

### Enter into container
```bash
make enter_container
```

### Lint

```bash 
make lint
```
### Format

```bash 
make format
```

### Test

If you want to run all tests, you can run the following command:
```bash 
make test
```

If you want to run the specific test, you can run the following command:
```bash
make enter_container

poetry shell

poe test tests/{file or directory you want to test}
```
