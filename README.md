<h1 align="center">🏦 - Mini Bank</h1>

###

<p align="left">Simulador de caixa eletrônico com as seguintes funções:<br><br>1. Abertura de conta<br>2. Depósito<br>3. Saque<br>4. Extrato / Saldo<br><br>*A base de dados foi desenvolvida utilizando manipulação de json's.</p>

###

<h2 align="left">📥 - Onde baixar</h2>

###

<p align="left">O link abaixo baixa a versão mais recente do repositório de modo estático.<br><br>https://github.com/vinnicius-martins/mini-bank/archive/refs/heads/master.zip</p>

###

<h2 align="left">👨‍💻 - Tecnologias Utilizadas</h2>

###

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" height="40" width="52" alt="python logo"  />
</div>

###

<h2 align="left">📚 - Bibliotecas utilizadas</h2>

###

<p align="left">json - Manipulação de json's.<br>os - Manipulação de arquivos.<br>datetime - Para uso do tipo data.<br>re - Utilização de expressões regulares.<br>time - Uso exclusivo da função sleep para implementar intervalo entre ações.</p>

###

<h2 align="left">▶️ - Como iniciar o sistema</h2>

###

<p align="left">1. Download do repositório zipado.<br>2. Extrair o repositorio para o caminho desejado.<br>3. Executar o arquivo __main__.py localizado na raiz do projeto.</p>

###

<h2 align="left">👣 - Passo a passo do sistema</h2>

###

<h3 align="left">Login / Cadastro</h3>

###

<p align="left">Ao iniciar, a tela observada deve ser semelhante a esta:</p>

###

<div align="left" >
  <img height="100" src="https://i.ibb.co/TWr7zW1/inicio.png"/>
</div>

###

<p align="left">Insira um CPF válido (existe verificação da estrutura)<br>* Caso queira, existe um gerador de CPF's online no link: https://www.4devs.com.br/gerador_de_cpf<br>** A pontuação no texto inserido é indiferente.<br><br>***Ao digitar "X" ou "SAIR" o sistema encerrará a execução.<br><br>Caso o CPF não esteja na base de dados, será solicitado o nome do usuário para cadastro:</p>

###

<div align="left" >
  <img height="40" src="https://i.ibb.co/svRR2Ms/nome.png"  />
</div>

###

<p align="left">Após o cadastro ou caso o CPF utilizado já esteja cadastrado, o login acontecerá e a tela mostrada será semelhante a esta:</p>

###

<div align="left">
  <img height="100" src="https://i.ibb.co/r6LXfhP/menu.png"  />
</div>

###

<p align="left">Nesse momento, insira o número correspondente ou o texto da opção desejada</p>

###

<br clear="both">

<h3 align="left">1 - Depósito</h3>

###

<div align="left">
  <img height="87" src="https://i.ibb.co/b635QTV/deposito.png"  />
</div>

###

<p align="left">Na tela de depósito, insira o valor desejado para depositar em sua conta ou deixe em branco para voltar ao menu principal.<br><br>*Como o caixa eletrônico trabalha apenas com notas, se o valor inserido contiver centavos o sistema dará a opção de continuar com o valor inteiro ou cancelar a operação.</p>

###

<br clear="both">

<h3 align="left">2 - Saque</h3>

###

<div align="left">
  <img height="100" src="https://i.ibb.co/jw856Y3/saque.png"  />
</div>

###

<p align="left">Na tela de saque, insira o valor desejado para saque ou deixe em branco para voltar ao menu principal.<br><br>*Como o caixa eletrônico trabalha apenas com notas, se o valor inserido contiver centavos o sistema dará a opção de continuar com o valor inteiro ou cancelar a operação.<br><br>**Caso o valor solicitado seja maior que o saldo atual do usuário, o sistema não permitirá a operação.</p>

###

<br clear="both">

<h3 align="left">3 - Extrato / Saldo</h3>

###

<p align="left">Caso não possua movimentação na conta, o sistema mostrará a tela abaixo:</p>

###

<div align="left">
  <img height="120" src="https://i.ibb.co/ygRrpvn/sem-extrato.png"  />
</div>

###

<p align="left">Caso possua movimentação, o sistema mostrará no console os registros das movimentações da conta.</p>

###

<div align="left">
  <img height="140" src="https://i.ibb.co/TbHkwkk/extrato.png"  />
</div>

###

<br clear="both">

<h3 align="left">4 - Logout</h3>

###

<p align="left">O sistema efetuará o logout e retornará para a pagina de solicitação de CPF para entrar.</p>

###

<div align="left">
  <img height="90" src="https://i.ibb.co/XpXFr91/logout.png"  />
</div>
