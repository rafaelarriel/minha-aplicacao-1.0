# Minha Aplicação

Aplicação simples em FastAPI, desenvolvida como exercício prático durante uma aula de DevOps do curso de pós-graduação em Ciência da Computação da UFLA.

## Executar com Docker

Com o Docker instalado e em execução, rode na raiz do projeto:

```bash
docker build -t minha-aplicacao:1.0 .
docker run --rm -p 8080:8000 minha-aplicacao:1.0
```

Acesse no navegador: [http://localhost:8080/hello](http://localhost:8080/hello).

A documentação da API está em [http://localhost:8080/docs](http://localhost:8080/docs).

O formato é `-p PORTA_DO_COMPUTADOR:PORTA_DO_CONTAINER`. Para usar outra porta no computador, troque `8080` no comando e na URL. Mantenha `8000` como porta do container.

O log do Uvicorn mostra `0.0.0.0:8000`, que é o endereço de escuta dentro do container. Para acessar pelo computador, use a URL com `localhost` acima.

Para parar, pressione `Ctrl+C` no terminal.

### Executar em segundo plano

```bash
docker run -d --rm --name minha-aplicacao -p 8080:8000 minha-aplicacao:1.0 \
  && echo "Aplicação disponível em http://localhost:8080/hello"
```

Para acompanhar os logs:

```bash
docker logs -f minha-aplicacao
```

Para parar o container:

```bash
docker stop minha-aplicacao
```

Após alterar o código, crie a imagem novamente e reinicie o container usando os comandos acima.
