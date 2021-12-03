# **API HoCo**

API RESTful do projeto [HoCo](https://github.com/Guardians-DSC/HoCo), que dispõe de funcionalidades *CRUD* de um sistema para gerenciamento de horas complementares dos alunos da graduação de Ciência da Computação na UFCG.

**Funcionalidades oferecidas pela API:**

**Minhas horas**
* [**Recupera o total de créditos do aluno**](#recupera-o-total-de-créditos-do-aluno)
* [**Recupera o número de horas por categoria do aluno**](#recupera-o-número-de-horas-por-categoria-do-aluno)
* [**Recupera as 4 categorias com o maior número de créditos do aluno**](#recupera-as-4-categorias-com-o-maior-número-de-créditos-do-aluno)

**Minhas atividades**
* [**Cadastra uma atividade do aluno**](#cadastra-uma-atividade-do-aluno)
* [**Lista as atividades cadastradas do aluno**](#lista-as-atividades-cadastradas-do-aluno)
* [**Edita uma atividade do aluno**](#edita-uma-atividade-do-aluno)
* [**Deleta uma atividade do aluno**](#deleta-uma-atividade-do-aluno)

**Organizações**
* [**Cadastra uma organização do curso**](#cadastra-uma-organização-do-curso)
* [**Lista as organizações do curso**](#lista-as-organizações-do-curso)
* [**Deleta uma organização do curso**](#deleta-uma-organização-do-curso)

**Dúvidas**
* [**Cadastra uma dúvida**](#cadastra-uma-dúvida)
* [**Lista as dúvidas**](#lista-as-dúvidas)
* [**Deleta uma dúvida**](#deleta-uma-dúvida)

## Recupera o total de créditos do aluno

Retorna um *JSON* contendo o número de créditos atual do aluno e o número máximo de créditos necessários no curso.

+ URL

```
GET /creditos
```

**Exemplo**

+ Request

```
curl -L -X GET 'https://hoco.netlify.app/creditos'
```

+ Response

```
Status: 200 OK
```
```
{
	"creditos": 11,
	"maximo": 22
}
```

## Recupera o número de horas por categoria do aluno

Retorna uma lista contendo o número de horas, por categoria, do aluno e o número máximo de créditos possíveis na categoria.

+ URL

```
GET /categorias/horas
```

**Exemplo**

+ Request

```
curl -L -X GET 'https://hoco.netlify.app/categorias/horas'
```

+ Response

```
Status: 200 OK
```
```
[
    {
		"categoria": "Projeto",
		"acumulado": 16,
		"maximo": 16
	},
    {
		"categoria": "Evento",
		"acumulado": 12,
		"maximo": 16
	},
    {
		"categoria": "Monitoria",
		"acumulado": 4,
		"maximo": 18
	},
    {
		"categoria": "Caesi",
		"acumulado": 2,
		"maximo": 4
	}
]
```

## Recupera as 4 categorias com o maior número de créditos do aluno

Retorna uma lista contendo as quatro categorias com o maior número de créditos do aluno, ordenadas pela porcentagem.

+ URL

```
GET /categorias/top
```

**Exemplo**

+ Request

```
curl -L -X GET 'https://hoco.netlify.app/categorias/top'
```

+ Response

```
Status: 200 OK
```
```
[
    {
	    "categoria": "Projeto",
	    "porcentagem": 0.45
	},
    {
		"categoria": "Evento",
		"porcentagem": 0.20
	},
    {
		"categoria": "Monitoria",
		"porcentagem": 0.10
	},
    {
		"categoria": "Caesi",
		"porcentagem": 0.10
	}
]
```

## Cadastra uma atividade do aluno

Adiciona no banco de dados uma atividade do aluno e retorna uma lista contendo todas as atividades adicionadas do aluno. A requisição deve enviar no body um *JSON* com os campos `titulo`, `creditos` e `categoria`.

+ URL

```
POST /atividade
```

+ Body

| Parameters | Type | Requirement | Description |
|---|---|---|---|
| `titulo` | String | obrigatório | o nome da atividade. |
| `creditos` | int | obrigatório | os créditos obtidos na atividade. |
| `categoria` | String | obrigatório | a categoria da atividade. |


**Exemplos**

+ Request

```
curl -L -X POST 'https://hoco.netlify.app/atividade' \
-H 'Content-Type: application/json' \
--data-raw '{
	    "titulo": "projeto ePol",
		"creditos": 10,
		"categoria": "Projeto"
    }
}'
```

+ Response

```
Status: 201 CREATED
```
```
[
	{
		"id:": 129087124908,
		"titulo": "projeto ePol",
		"creditos": 10,
		"categoria": "Projeto"
	},
    {
		"id:": 129087124901,
		"titulo": "CodeSQ",
		"creditos": 4,
		"categoria": "Projeto"
	},
    {
		"id:": 132312312312,
		"titulo": "Andromedev",
		"horas": 135,
		"categoria": "Evento"
	}
]
```

## Lista as atividades cadastradas do aluno

Retorna uma lista contendo todas as atividades adicionadas do aluno.

+ URL

```
GET /atividades
```

**Exemplo**

+ Request

```
curl -L -X GET 'https://hoco.netlify.app/atividades'
```

+ Response

```
Status: 200 OK
```
```
[
	{
		"id:": 129087124908,
		"titulo": "projeto ePol",
		"creditos": 10,
		"categoria": "Projeto"
	},
    {
		"id:": 129087124901,
		"titulo": "CodeSQ",
		"creditos": 4,
		"categoria": "Projeto"
	},
    {
		"id:": 132312312312,
		"titulo": "Andromedev",
		"horas": 135,
		"categoria": "Evento"
	}
]
```

## Edita uma atividade do aluno

Atualiza no banco de dados as informações de uma atividade do aluno e retorna uma lista contendo todas as atividades atuais do aluno. O ID da atividade deve ser informado na URL. A requisição deve enviar no body um *JSON* contendo os campos de possível edição, sendo estes: `titulo`, `creditos` e `categoria`.

+ URL

```
PATCH /atividade/<atividade_id>
```

| Parameters | Type | Requirement | Description |
|---|---|---|---|
| `atividade_id` | String | obrigatório | o id da atividade. |

+ Body

| Parameters | Type | Requirement | Description |
|---|---|---|---|
| `titulo` | String | opcional | o nome da atividade. |
| `creditos` | int | opcional | os créditos obtidos na atividade. |
| `categoria` | String | opcional | a categoria da atividade. |

**Exemplos**

+ Request

```
curl -L -X PATCH 'https://hoco.netlify.app/atividade/129087124908' \
-H 'Content-Type: application/json' \
--data-raw '{
    "creditos": 12
}'
```

+ Response

```
Status: 200 OK
```
```
[
	{
		"id:": 129087124908,
		"titulo": "projeto ePol",
		"creditos": 12,
		"categoria": "Projeto"
	},
    {
		"id:": 129087124901,
		"titulo": "CodeSQ",
		"creditos": 4,
		"categoria": "Projeto"
	},
    {
		"id:": 132312312312,
		"titulo": "Andromedev",
		"horas": 135,
		"categoria": "Evento"
	}
]
```

## Deleta uma atividade do aluno

Deleta do banco de dados uma atividade do aluno e retorna uma lista contendo todas as atividades restantes do aluno. O ID da atividade deve ser informado na URL.

+ URL

```
DELETE /atividade/<atividade_id>
```

| Parameters | Type | Requirement | Description |
|---|---|---|---|
| `atividade_id` | String | obrigatório | o id da atividade. |

**Exemplos**

+ Request

```
curl -L -X DELETE 'https://hoco.netlify.app/atividade/129087124908'
```

+ Response

```
Status: 200 OK
```
```
[
    {
		"id:": 129087124901,
		"titulo": "CodeSQ",
		"creditos": 4,
		"categoria": "Projeto"
	},
    {
		"id:": 132312312312,
		"titulo": "Andromedev",
		"horas": 135,
		"categoria": "Evento"
	}
]
```

## Cadastra uma organização do curso

Adiciona no banco de dados uma organização do curso e retorna uma lista contendo todas as organizações adicionadas do curso. A requisição deve enviar no body um *JSON* com o campo `organizacao`.

+ URL

```
POST /organizacao
```

+ Body

| Parameters | Type | Requirement | Description |
|---|---|---|---|
| `organizacao` | String | obrigatório | o nome da organização. |

**Exemplos**

+ Request

```
curl -L -X POST 'https://hoco.netlify.app/organizacao' \
-H 'Content-Type: application/json' \
--data-raw '{
	    "organizacao": "OpenDevUFCG"
    }
}'
```

+ Response

```
Status: 201 CREATED
```
```
[
	{
		"id": 122,
		"organizacao": "OpenDevUFCG",
		"imagem": "img.jpg"
	},
	{
		"id": 123,
		"organizacao": "Pet@Computação",
		"imagem": "img.jpg"
	},
	{
		"id": 124,
		"organizacao": "Caesi",
		"imagem": "img.jpg"
	},
	{
		"id": 125,
		"organizacao": "Guardians",
		"imagem": "img.jpg"
	},
	{
		"id": 126,
		"organizacao": "Elas@Computação",
		"imagem": "img.jpg"
	},
]
```

## Lista as organizações do curso

Retorna uma lista contendo todas as organizações adicionadas do curso.

+ URL

```
GET /organizacoes
```

**Exemplo**

+ Request

```
curl -L -X GET 'https://hoco.netlify.app/organizacoes'
```

+ Response

```
Status: 200 OK
```
```
[
	{
		"organizacao": "OpenDevUFCG",
		"imagem": "img.jpg"
	},
	{
		"organizacao": "Pet@Computação",
		"imagem": "img.jpg"
	},
	{
		"organizacao": "Caesi",
		"imagem": "img.jpg"
	},
	{
		"organizacao": "Guardians",
		"imagem": "img.jpg"
	},
	{
		"organizacao": "Elas@Computação",
		"imagem": "img.jpg"
	},
]
```

## Deleta uma organização do curso

Deleta do banco de dados uma organização do curso e retorna uma lista contendo todas as organizações restantes do curso. O ID da organização deve ser informado na URL.

+ URL

```
DELETE /organizacao/<organizacao_id>
```

| Parameters | Type | Requirement | Description |
|---|---|---|---|
| `organizacao_id` | String | obrigatório | o id da organização. |

**Exemplos**

+ Request

```
curl -L -X DELETE 'https://hoco.netlify.app/organizacao/123'
```

+ Response

```
Status: 200 OK
```
```
[
	{
		"id": 122,
		"organizacao": "OpenDevUFCG",
		"imagem": "img.jpg"
	},
	{
		"id": 124,
		"organizacao": "Caesi",
		"imagem": "img.jpg"
	},
	{
		"id": 125,
		"organizacao": "Guardians",
		"imagem": "img.jpg"
	},
	{
		"id": 126,
		"organizacao": "Elas@Computação",
		"imagem": "img.jpg"
	},
]
```

## Cadastra uma dúvida

## Lista as dúvidas

## Deleta uma dúvida
