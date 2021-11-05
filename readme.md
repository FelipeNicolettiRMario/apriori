# Sistema de Aprendizado Não Supervisionado Apriori

### Alunos:
- Felipe Nicoletti Reis Mario
- Gabriel Fernandes Giraud

## Baixando dependencias

Para baixar dependências bastar executar o seguinte comando:

```pip install -r requirements.txt```

## Configurando o banco de dados

Para esse projeto é necessário popular o banco de dados na pasta input, para isso basta rodar o seguinte comando:

```python csv-to-mariadb.py```

## Setando Variáveis de ambiente

Para o funcionamento do projeto é necessário que sejam setado
variáveis de ambiente em um arquivo '.env' na raiz do projeto.
Os dados que precisam ser setados terão que ter esse modelo

```
BD_URI=mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}
```

## Executando os programa

Para a execução do programa basta rodar o seguinte comando:

```python explore-data.py```

Três indicadores serão gerados no matplotlib, após isso será mostrado as duas regras de associação mais fortes da base.
