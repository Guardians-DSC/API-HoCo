# **API HoCo**

API RESTful do projeto [HoCo](https://github.com/Guardians-DSC/HoCo), que dispõe de funcionalidades _CRUD_ de um sistema para gerenciamento de horas complementares dos alunos da graduação de Ciência da Computação na UFCG.

## **Funcionalidades oferecidas pela API:**

### **Minhas horas**

- [**Recupera o total de créditos do aluno**](#recupera-o-total-de-creditos-do-aluno)
- [**Recupera o total de créditos por categoria do aluno**](#recupera-o-total-de-creditos-por-categoria-do-aluno)
- [**Recupera as 4 categorias com o maior número de créditos do aluno**](#recupera-as-4-categorias-com-o-maior-numero-de-creditos-do-aluno)

### **Minhas atividades**

- [**Cadastra uma atividade do aluno**](#cadastra-uma-atividade-do-aluno)
- [**Lista as atividades cadastradas do aluno**](#lista-as-atividades-cadastradas-do-aluno)
- [**Edita uma atividade do aluno**](#edita-uma-atividade-do-aluno)
- [**Remove uma atividade do aluno**](#remove-uma-atividade-do-aluno)

### **Organizações**

- [**Cadastra uma organização do curso**](#cadastra-uma-organizacao-do-curso)
- [**Lista as organizações do curso**](#lista-as-organizacoes-do-curso)
- [**Remove uma organização do curso**](#remove-uma-organizaçao-do-curso)

### **Dúvidas**

- [**Cadastra uma dúvida**](#cadastra-uma-duvida)
- [**Lista as dúvidas**](#lista-as-duvidas)
- [**Remove uma dúvida**](#remove-uma-duvida)

## Recupera o total de creditos do aluno

Retorna um _JSON_ contendo o número de créditos atual do aluno e o número máximo de créditos necessários no curso.

#### URL

```
GET /credits
```

**Exemplo**

#### Request

```
curl -L -X GET 'https://hoco.netlify.app/credits'
```

#### Response

```
Status: 200 OK
```

```
{
	"creditos": 11,
	"maximo": 22
}
```

## Recupera o total de creditos por categoria do aluno

Retorna uma lista contendo o total de créditos acumulados, por categoria, do aluno e o número máximo de créditos possíveis na categoria, ordenado de forma decrescente a partir da categoria de maior proporção para a de menor proporção na proporção total.

#### URL

```
GET /categories/
```

**Exemplo**

#### Request

```
curl -L -X GET 'https://hoco.netlify.app/categories/'
```

#### Response

```
Status: 200 OK
```

```
[
    {
		"category": "Projeto",
		"amount": 16,
		"max": 16,
		"category_piece": 0.20
	},
    {
		"category": "Evento",
		"amount": 12,
		"max": 16,
		"category_piece": 0.18
	},
    {
		"category": "Monitoria",
		"amount": 4,
		"max": 18,
		"category_piece": 0.15
	},
    {
		"category": "Caesi",
		"amount": 2,
		"max": 4,
		"category_piece": 0.10
	}
]
```

## Cadastra uma atividade do aluno

Adiciona no banco de dados uma atividade do aluno e retorna uma lista contendo todas as atividades adicionadas do aluno. A requisição deve enviar no body um _JSON_ com os campos `title`, `credits`, `time (horas)` e `category`.

#### URL

```
POST /activity
```

#### Body

| Parameters | Type   | Requirement | Description                       |
| ---------- | ------ | ----------- | --------------------------------- |
| `title`    | String | obrigatório | o nome da atividade.              |
| `credits`  | int    | obrigatório | os créditos obtidos na atividade. |
| `time`     | int    | obrigatório | as horas gastas na atividade.     |
| `category` | String | obrigatório | a categoria da atividade.         |

**Exemplos**

#### Request

```
curl -L -X POST 'https://hoco.netlify.app/activity' \
-H 'Content-Type: application/json' \
--data-raw '{
	    "titulo": "projeto ePol",
		"creditos": 10,
		"categoria": "Projeto"
    }
}'
```

#### Response

```
Status: 201 CREATED
```

```
[
	{
		"id:": 129087124908,
		"title": "projeto ePol",
		"credits": 10,
		"category": "Projeto"
	},
    {
		"id:": 129087124901,
		"title": "CodeSQ",
		"time": 320,
		"category": "Projeto"
	},
    {
		"id:": 132312312312,
		"title": "Andromedev",
		"time": 135,
		"category": "Evento"
	}
]
```

## Lista as atividades cadastradas do aluno

Retorna uma lista contendo todas as atividades adicionadas do aluno.

#### URL

```
GET /activities
```

**Exemplo**

#### Request

```
curl -L -X GET 'https://hoco.netlify.app/activities'
```

#### Response

```
Status: 200 OK
```

```
[
	{
		"id:": 129087124908,
		"title": "projeto ePol",
		"credits": 10,
		"category": "Projeto"
	},
    {
		"id:": 129087124901,
		"title": "CodeSQ",
		"credits": 4,
		"category": "Projeto"
	},
    {
		"id:": 132312312312,
		"title": "Andromedev",
		"time": 135,
		"category": "Evento"
	}
]
```

## Edita uma atividade do aluno

Atualiza no banco de dados as informações de uma atividade do aluno e retorna uma lista contendo todas as atividades atuais do aluno. O ID da atividade deve ser informado na URL. A requisição deve enviar no body um _JSON_ contendo os campos de possível edição, sendo estes: `title`, `credits`, `time (horas)` e `category`.

#### URL

```
PATCH /activity?id=<atividade_id>
```

| Parameters    | Type   | Requirement | Description        |
| ------------- | ------ | ----------- | ------------------ |
| `activity_id` | String | obrigatório | o id da atividade. |

#### Body

| Parameters | Type   | Requirement | Description                       |
| ---------- | ------ | ----------- | --------------------------------- |
| `title`    | String | opcional    | o nome da atividade.              |
| `credits`  | int    | opcional    | os créditos obtidos na atividade. |
| `time`     | int    | opcional    | as horas gastas na atividade.     |
| `category` | String | opcional    | a categoria da atividade.         |

**Exemplos**

#### Request

```
curl -L -X PATCH 'https://hoco.netlify.app/activity?id=129087124908' \
-H 'Content-Type: application/json' \
--data-raw '{
    "creditos": 12
}'
```

#### Response

```
Status: 200 OK
```

```
[
	{
		"id:": 129087124908,
		"title": "projeto ePol",
		"credits": 12,
		"time": 950,
		"category": "Projeto"
	},
    {
		"id:": 129087124901,
		"title": "CodeSQ",
		"credits": 4,
		"time": 320,
		"category": "Projeto"
	},
    {
		"id:": 132312312312,
		"title": "Andromedev",
		"time": 135,
		"category": "Evento"
	}
]
```

## Remove uma atividade do aluno

Deleta do banco de dados uma atividade do aluno e retorna uma lista contendo todas as atividades restantes do aluno. O ID da atividade deve ser informado na URL.

#### URL

```
DELETE /atividade?id=<atividade_id>
```

| Parameters     | Type   | Requirement | Description        |
| -------------- | ------ | ----------- | ------------------ |
| `atividade_id` | String | obrigatório | o id da atividade. |

**Exemplos**

#### Request

```
curl -L -X DELETE 'https://hoco.netlify.app/activity?id=129087124908'
```

#### Response

```
Status: 200 OK
```

```
[
    {
		"id:": 129087124901,
		"title": "CodeSQ",
		"credits": 4,
		"category": "Projeto"
	},
    {
		"id:": 132312312312,
		"title": "Andromedev",
		"time": 135,
		"category": "Evento"
	}
]
```

## Cadastra uma organização do curso

Adiciona no banco de dados uma organização do curso e retorna uma lista contendo todas as organizações adicionadas do curso.

#### URL

```
POST /org
```

#### Body

**Content-type**: Multipart Form

| Parameters | Type   | Requirement | Description                                    |
| ---------- | ------ | ----------- | ---------------------------------------------- |
| `name`     | String | obrigatório | o nome da organização.                         |
| `org_url`  | String | obrigatório | Url de acesso da organização na web.           |
| `image`    | File   | obrigatório | Arquivo de imagem representante da organização |

**Exemplos**

#### Request

```
curl -L -X POST 'https://hoco.netlify.app/org' \
	-H 'Content-Type: form-data' \
	-F name='nome'\
	-F org_url=url'\
	-F image <caminho/para/arquivo>
}'
```

#### Response

```
Status: 201 CREATED
```

```
{
	"_id": 1231231231231232,
	"name": "OpenDevUFCG",
	"org_url": "<URL>",
	"image": <coded_image>
}
```

## Lista as organizacoes do curso

Retorna uma lista contendo todas as organizações adicionadas do curso.

#### URL

```
GET /orgs
```

**Exemplo**

#### Request

```
curl -L -X GET 'https://hoco.netlify.app/orgs'
```

#### Response

```
Status: 200 OK
```

```
[
	{
		"_id": 1231231231231232,
		"name": "OpenDevUFCG",
		"org_url": "<URL>",
		"image": <coded_image>
	},
	{
		"_id": 1231231231231232,
		"name": "Pet@Computação",
		"org_url": "<URL>",
		"image": <coded_image>
	},
	{
		"_id": 1231231231231232,
		"name": "Caesi",
		"org_url": "<URL>",
		"image": <coded_image>
	},
	{
		"_id": 1231231231231232,
		"name": "Guardians",
		"org_url": "<URL>",
		"image": <coded_image>
	},
	{
		"_id": 1231231231231232,
		"name": "Elas@Computação",
		"org_url": "<URL>",
		"image": <coded_image>
	}
]
```

## Remove uma organizacao do curso

Deleta do banco de dados uma organização do curso e retorna uma lista contendo todas as organizações restantes do curso. O ID da organização deve ser informado na URL.

#### URL

```
DELETE /org?id=<org_id>
```

| Parameters | Type   | Requirement | Description                          |
| ---------- | ------ | ----------- | ------------------------------------ |
| `id`       | String | obrigatório | id da organização no banco de dados. |

**Exemplos**

#### Request

```
curl -L -X DELETE 'https://hoco.netlify.app/org?id=62a60f4fc230515f63abae43'
```

#### Response

```
Status: 200 OK
```

```
[
	{
		"_id": 1231231231231232,
		"name": "Pet@Computação",
		"org_url": "<URL>",
		"image": <coded_image>
	},
	{
		"_id": 1231231231231232,
		"name": "Caesi",
		"org_url": "<URL>",
		"image": <coded_image>
	},
	{
		"_id": 1231231231231232,
		"name": "Guardians",
		"org_url": "<URL>",
		"image": <coded_image>
	},
	{
		"_id": 1231231231231232,
		"name": "Elas@Computação",
		"org_url": "<URL>",
		"image": <coded_image>g"
	}
]
`
```

## Cadastra uma duvida

Adiciona no banco de dados uma dúvida sobre o curso com a respectiva resposta e retorna uma lista contendo todas as dúvidas adicionadas sobre o curso. A requisição deve enviar no body um _JSON_ com os campos `question` e `answer`.

#### URL

```
POST /question
```

#### Body

| Parameters | Type   | Requirement | Description                         |
| ---------- | ------ | ----------- | ----------------------------------- |
| `question` | String | obrigatório | a dúvida sobre o curso.             |
| `answer`   | String | obrigatório | a resposta da dúvida sobre o curso. |

**Exemplos**

#### Request

```
curl -L -X POST 'https://hoco.netlify.app/question' \
-H 'Content-Type: application/json' \
--data-raw '{
	    "question": "[a pergunta aqui]",
			"answer": "[a resposta aqui]"
    }
}'
```

#### Response

```
Status: 201 CREATED
```

```
{
	"_id": 12345,
	"question": "[a pergunta aqui]",
	"answer": "[a resposta aqui]"
}
```

## Lista as duvidas

Retorna uma lista contendo todas as dúvidas adicionadas sobre o curso.

#### URL

```
GET /questions
```

**Exemplo**

#### Request

```
curl -L -X GET 'https://hoco.netlify.app/questions'
```

#### Response

```
Status: 200 OK
```

```
[
	{
		"_id": 12345,
		"question": "[a pergunta aqui]",
		"answer": "[a resposta aqui]"
	},
	{
		"_id": 12678,
		"question": "[a pergunta aqui]",
		"answer": "[a resposta aqui]"
	},
	{
		"_id": 12901,
		"question": "[a pergunta aqui]",
		"answer": "[a resposta aqui]"
	}
]
```

## Remove uma duvida

Deleta do banco de dados uma dúvida sobre o curso e retorna uma lista contendo todas as dúvidas restantes sobre o curso. O ID da organização deve ser informado na URL.

#### URL

```
DELETE /question?id=<question_id>
```

| Parameters    | Type   | Requirement | Description           |
| ------------- | ------ | ----------- | --------------------- |
| `question_id` | String | obrigatório | o id da dúvida no bd. |

**Exemplos**

#### Request

```
curl -L -X DELETE 'https://hoco.netlify.app/question?id=12345'
```

#### Response

```
Status: 200 OK
```

```
[
	{
		"_id": 12678,
		"question": "[a pergunta aqui]",
		"answer": "[a resposta aqui]"
	},
	{
		"_id": 12901,
		"question": "[a pergunta aqui]",
		"answer": "[a resposta aqui]"
	}
]
```
