# Quem e como posso contribuir?
Qualquer pessoa pode contribuir com esse projeto ao criar uma issue de uma nova funcionalidade (feature request) ou de aviso de bugs (bug report). Além disso, é possível enviar PRs que estejam relacionados a uma issue existente. Tais PRs serão revisadas por mim (Eduardo Vítor), antes de serem aprovados.

## O projeto adota alguma convenção de nomes de variáveis/métodos/classes?

Sim! O projeto atualmente utiliza a convenção de nomes do Python presente nesse [link](https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html).

## Como configurar o ambiente de desenvolvimento
As funções para extração de notícias são escritas em [Python](https://www.python.org/). Logo, você deve ter um ambiente de desenvolvimento [Python](https://www.python.org/) instalado em seu computador de acordo com as instruções de instalação para o seu sistema Windows/Linux/Mac. Para adicionar uma nova função de extração de notícias, execute os passos a seguir: 

### Windows/Linux/Mac
1. Faça um fork deste repositório e, com o terminal aberto em um diretório de preferência no seu computador, clone-o e acesse o novo diretório criado com o nome do repositório.
``` console
git clone <repositorio_fork>
cd ArapiracaNewsBot
```

2. Instale as [bibliotecas requeridas](https://github.com/eduardovitor/ArapiracaNewsBot/blob/master/requirements.txt).
``` console
pip install -r requirements.txt
```
3. Edite o arquivo ```arapiracanews.py``` na sua IDE de preferência para implementar uma nova função de extração.

4. Antes de enviar um Pull Request (PR), teste sua função de extração manualmente ao chamá-la dentro do arquivo ```arapiracanews.py```.

``` console
python3 arapiracanews.py
```

5. Por fim, verifique se seu código passa nos testes unitários do projeto ao executar:

``` console
python3 test/tests_suite.py
```

Obs: Após a aprovação do PR, a funcionalidade será incorporada por mim (Eduardo Vítor) no ```main.py``` que contém a comunicação do bot com a API do Telegram e os comandos que podem ser acessados por meio do bot.