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
	"maximo": 22,
}
```

## Recupera o número de horas por categoria do aluno

Retorna uma lista contendo o número de horas do aluno por categoria e o número máximo de créditos possíveis na categoria.

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
		"maximo": 16,
	},
    {
		"categoria": "Evento",
		"acumulado": 12,
		"maximo": 16,
	},
    {
		"categoria": "Monitoria",
		"acumulado": 4,
		"maximo": 18,
	},
    {
		"categoria": "Caesi",
		"acumulado": 2,
		"maximo": 4,
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
	    "porcentagem": 0.45,
    },
    {
		"categoria": "Evento",
		"porcentagem": 0.20,
	},
    {
		"categoria": "Monitoria",
		"porcentagem": 0.10,
	},
    {
		"categoria": "Caesi",
		"porcentagem": 0.10,
    }
]
```

## Cadastra uma atividade do aluno

## Lista as atividades cadastradas do aluno

## Edita uma atividade do aluno

## Deleta uma atividade do aluno

## Cadastra uma organização do curso

## Lista as organizações do curso

## Deleta uma organização do curso

## Cadastra uma dúvida

## Lista as dúvidas

## Deleta uma dúvida