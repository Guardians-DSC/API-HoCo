# Exemplo de API com Flask

Esse repositório serve para ilustrar a construção de APIs com Flask em Python. Testes com utilizando a biblioteca Pytest também foram adicionados.

## Como executar a API

Para executar, é preciso ter as dependências (Flask e Pytest) instaladas e executar o seguinte comando:

```
python3 -m backend
```

Você pode optar por instalar as dependências direto na sua máquina com o pip, ou utilizar um ambiente virtual (fortemente recomendado).

## Como executar os testes

Basta utilizar o comando:

```
python3 -m pytest
```

## Ambientes virtuais

### Para que servem?

Um ambiente virtual serve para que seja possível encapsular os pacotes utilizados na API a fim de que eles não "poluam" sua máquina. Utilizar esses ambientes também se mostram úteis no processo de automatização da instalação das dependências do projeto, além de evitar interferências em pacotes de outros projetos.

### Como criar um ambiente virtual e instalar os pacotes:

1. Crie o ambiente virtual
```
python3 -m venv venv
```

2. Ative o ambiente virtual
```
source venv/bin/activate
```

3. Instale os pacotes (Flask e Pytest) presentes no requirements.txt
```
pip install -r requirements.txt
```
> Para desativar o ambiente virtual, basta digitar o comando `deactivate`
