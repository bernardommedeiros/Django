# Recebe e envia dados dada a requisição do user

## Metodos
- POST:
 ### Uso
 <p>enviar dados ao servidor, afim de processá-los no banco de dados.</p>

 <br>

 - são enviados na solicitação HTTP, não visivel.
  - sem limite de tamanho de dados.
 - ideal para operações que alteram dados no servidor (ex: forms).
 - não pode ser armazenado em cache ou mantido no histórico do navegador.

<br>

 - GET:
 ### Uso
 <p>recupera dados</p>

 <br>

 - são enviados na solicitação URL, visivel ao user.
 - tamanho de dados limitado.
 - ideal para operações que não alteram dados (ex: busca/pesquisa).
 - armazenado em cache ou mantido no histórico do navegador.