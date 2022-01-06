# **API HoCo**

API RESTful do projeto [HoCo](https://github.com/Guardians-DSC/HoCo), que dispõe de funcionalidades *CRUD* de um sistema para gerenciamento de horas complementares dos alunos da graduação de Ciência da Computação na UFCG.

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

Retorna um *JSON* contendo o número de créditos atual do aluno e o número máximo de créditos necessários no curso.

#### URL

```
GET /creditos
```

**Exemplo**

#### Request

```
curl -L -X GET 'https://hoco.netlify.app/creditos'
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

Retorna uma lista contendo o total de créditos acumulados, por categoria, do aluno e o número máximo de créditos possíveis na categoria.

#### URL

```
GET /categorias/creditos
```

**Exemplo**

#### Request

```
curl -L -X GET 'https://hoco.netlify.app/categorias/creditos'
```

#### Response

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

## Recupera as 4 categorias com o maior numero de creditos do aluno

Retorna uma lista contendo as quatro categorias com o maior número de créditos do aluno, ordenadas pela porcentagem.

#### URL

```
GET /categorias/top
```

**Exemplo**

#### Request

```
curl -L -X GET 'https://hoco.netlify.app/categorias/top'
```

#### Response

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

Adiciona no banco de dados uma atividade do aluno e retorna uma lista contendo todas as atividades adicionadas do aluno. A requisição deve enviar no body um *JSON* com os campos `titulo`, `creditos`, `horas` e `categoria`.

#### URL

```
POST /atividade
```

#### Body

| Parameters | Type | Requirement | Description |
|---|---|---|---|
| `titulo` | String | obrigatório | o nome da atividade. |
| `creditos` | int | obrigatório | os créditos obtidos na atividade. |
| `horas` | int | obrigatório | as horas gastas na atividade. |
| `categoria` | String | obrigatório | a categoria da atividade. |

**Exemplos**

#### Request

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

#### Response

```
Status: 201 CREATED
```
```
[
	{
		"id:": 129087124908,
		"titulo": "projeto ePol",
		"creditos": 10,
		"horas": 950,
		"categoria": "Projeto"
	},
    {
		"id:": 129087124901,
		"titulo": "CodeSQ",
		"creditos": 4,
		"horas": 320,
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

#### URL

```
GET /atividades
```

**Exemplo**

#### Request

```
curl -L -X GET 'https://hoco.netlify.app/atividades'
```

#### Response

```
Status: 200 OK
```
```
[
	{
		"id:": 129087124908,
		"titulo": "projeto ePol",
		"creditos": 10,
		"horas": 950,
		"categoria": "Projeto"
	},
    {
		"id:": 129087124901,
		"titulo": "CodeSQ",
		"creditos": 4,
		"horas": 320,
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

Atualiza no banco de dados as informações de uma atividade do aluno e retorna uma lista contendo todas as atividades atuais do aluno. O ID da atividade deve ser informado na URL. A requisição deve enviar no body um *JSON* contendo os campos de possível edição, sendo estes: `titulo`, `creditos`, `horas` e `categoria`.

#### URL

```
PATCH /atividade?id=<atividade_id>
```

| Parameters | Type | Requirement | Description |
|---|---|---|---|
| `atividade_id` | String | obrigatório | o id da atividade. |

#### Body

| Parameters | Type | Requirement | Description |
|---|---|---|---|
| `titulo` | String | opcional | o nome da atividade. |
| `creditos` | int | opcional | os créditos obtidos na atividade. |
| `horas` | int | opcional | as horas gastas na atividade. |
| `categoria` | String | opcional | a categoria da atividade. |

**Exemplos**

#### Request

```
curl -L -X PATCH 'https://hoco.netlify.app/atividade?id=129087124908' \
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
		"titulo": "projeto ePol",
		"creditos": 12,
		"horas": 950,
		"categoria": "Projeto"
	},
    {
		"id:": 129087124901,
		"titulo": "CodeSQ",
		"creditos": 4,
		"horas": 320,
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

## Remove uma atividade do aluno

Deleta do banco de dados uma atividade do aluno e retorna uma lista contendo todas as atividades restantes do aluno. O ID da atividade deve ser informado na URL.

#### URL

```
DELETE /atividade?id=<atividade_id>
```

| Parameters | Type | Requirement | Description |
|---|---|---|---|
| `atividade_id` | String | obrigatório | o id da atividade. |

**Exemplos**

#### Request

```
curl -L -X DELETE 'https://hoco.netlify.app/atividade?id=129087124908'
```

#### Response

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

#### URL

```
POST /organizacao
```

#### Body

| Parameters | Type | Requirement | Description |
|---|---|---|---|
| `organizacao` | String | obrigatório | o nome da organização. |

**Exemplos**

#### Request

```
curl -L -X POST 'https://hoco.netlify.app/organizacao' \
-H 'Content-Type: application/json' \
--data-raw '{
	    "organizacao": "OpenDevUFCG"
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
	}
]
```

## Lista as organizacoes do curso

Retorna uma lista contendo todas as organizações adicionadas do curso.

#### URL

```
GET /organizacoes
```

**Exemplo**

#### Request

```
curl -L -X GET 'https://hoco.netlify.app/organizacoes'
```

#### Response

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
	}
]
```

## Remove uma organizacao do curso

Deleta do banco de dados uma organização do curso e retorna uma lista contendo todas as organizações restantes do curso. O ID da organização deve ser informado na URL.

#### URL

```
DELETE /organizacao?id=<organizacao_id>
```

| Parameters | Type | Requirement | Description |
|---|---|---|---|
| `organizacao_id` | String | obrigatório | o id da organização. |

**Exemplos**

#### Request

```
curl -L -X DELETE 'https://hoco.netlify.app/organizacao?id=123'
```

#### Response

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
	}
]
```

## Cadastra uma duvida

Adiciona no banco de dados uma dúvida sobre o curso com a respectiva resposta e retorna uma lista contendo todas as dúvidas adicionadas sobre o curso. A requisição deve enviar no body um *JSON* com os campos `pergunta` e `resposta`.

#### URL

```
POST /duvida
```

#### Body

| Parameters | Type | Requirement | Description |
|---|---|---|---|
| `pergunta` | String | obrigatório | a dúvida sobre o curso. |
| `resposta` | String | obrigatório | a resposta da dúvida sobre o curso. |

**Exemplos**

#### Request

```
curl -L -X POST 'https://hoco.netlify.app/duvida' \
-H 'Content-Type: application/json' \
--data-raw '{
	    "pergunta": "[a pergunta aqui]",
		"resposta": "[a resposta aqui]"
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
		"id": 12345,
		"pergunta": "[a pergunta aqui]",
		"resposta": "[a resposta aqui]"
	},
	{
		"id": 12678,
		"pergunta": "[a pergunta aqui]",
		"resposta": "[a resposta aqui]"
	},
	{
		"id": 12901,
		"pergunta": "[a pergunta aqui]",
		"resposta": "[a resposta aqui]"
	}
]
```

## Lista as duvidas

Retorna uma lista contendo todas as dúvidas adicionadas sobre o curso.

#### URL

```
GET /duvidas
```

**Exemplo**

#### Request

```
curl -L -X GET 'https://hoco.netlify.app/duvidas'
```

#### Response

```
Status: 200 OK
```
```
[
	{
		"id": 12345,
		"pergunta": "[a pergunta aqui]",
		"resposta": "[a resposta aqui]"
	},
	{
		"id": 12678,
		"pergunta": "[a pergunta aqui]",
		"resposta": "[a resposta aqui]"
	},
	{
		"id": 12901,
		"pergunta": "[a pergunta aqui]",
		"resposta": "[a resposta aqui]"
	}
]
```

## Remove uma duvida

Deleta do banco de dados uma dúvida sobre o curso e retorna uma lista contendo todas as dúvidas restantes sobre o curso. O ID da organização deve ser informado na URL.

#### URL

```
DELETE /duvida?id=<duvida_id>
```

| Parameters | Type | Requirement | Description |
|---|---|---|---|
| `duvida_id` | String | obrigatório | o id da organização. |

**Exemplos**

#### Request

```
curl -L -X DELETE 'https://hoco.netlify.app/duvida?id=12345'
```

#### Response

```
Status: 200 OK
```
```
[
	{
		"id": 12678,
		"pergunta": "[a pergunta aqui]",
		"resposta": "[a resposta aqui]"
	},
	{
		"id": 12901,
		"pergunta": "[a pergunta aqui]",
		"resposta": "[a resposta aqui]"
	}
]
```
