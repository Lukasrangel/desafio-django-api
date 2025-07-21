Desafio Nivelamento Django API Docker


<h2> Desafio criado para nivelar conhecimento do grupo </h2>

a ideia é que cada um faça um fork deste repositório, crie uma branch com o seu nome e ao finalizar mandar um pull request

Este repo contém Dockerfile e docker-compose.yml e uma base para o desafio com o app Produtos

<h3> Ambiente </h3>


O docker compose criará dois containers, um para o banco de dados postgres e outro usa como base o dockerfile para criar um container simples com python + django instalados
o arquivo requirements é o arquivo de pacotes iniciais da instalação do django, sempre que o container web subir vai instalar as dependências escritas ali.

para dar um start no projeto só rodar docker compose up --build

roda o projeto na porta 8000

para testar os endpoints recomendo usar isomnia ou postman


<h3> Desenvolver uma API para um ecommerce simples </h3>

<h4> Apps </h4>

Este projeto já possui o app Produtos, orientado a objetos com os metodos get e post,  <br>
post recebe nome e preço e salva o produto no db <br>
get lista os produtos cadastrados.

Existe um arquivo chamado serializers.py, este arquivo é usado para fazer as validações dos dados enviados para a API.

Existe um arquivo no core do projeto chaado utils.py com a classe JsonResponseHelper, essa classe é feita para ser usada no retorno das chamadas ao endpoint, 
ela serve para organizar e padronizar as respostas da API, para que toda a resposta tenha o mesmo padrão.

Podendo utilizar o mesmo padrão do app Produtos, o desafio é criar um app chamado clientes com os métodos get e post sendo get para listar clientes e post 
para cadastrar um cliente, usando serializer.py dentro do app para validar os dados e utilizando JsonResponseHelper para retornar os dados da API.

criar um app chamado pedidos, com três endpoints, um para consultar todos os pedidos, outro para consultar todos os pedidos de um usuario, 
e um endpoint post para criar um pedido.

Dica para pedidos, criar uma tabela itens_pedidos que faz a relação entre o pedido e o item, para cada linha da tabela é uma relação entre item e pedido
 

