# Realizar login no site, baixar e manipular arquivos

O que fazer quando a empresa não disponibilizar uma API para você poder consumir? <br><br>
Após alguns dias pesquisando e avaliando as alternativas de como automatizar esse processo, me deparei com Selenium, uma biblioteca poderosa. Com ela é possível realizar autenticação, ações como: navegar no site e baixar arquivos. E é o que essa automatização se propõe a fazer.

### Assista o vídeo mostrando como funciona:

[![AUTOMATIZAÇÃO PYTHON](https://github.com/marquescharlon/WebScraping-Selenium-Python/blob/main/img/capa_automatizacao_python.png)](https://www.youtube.com/watch?v=fsYzNT58RUw)

## Parâmetros
Vou destacar aqui os parâmetros principais, os que conversam diretamente com o Selenium. Para isso, acesse o arquivo ```parameters.py```<br>

Para definir o endereço do site basta atribuí-lo na variável ```link=''```.
Se o endereço da página onde os arquivos estiverem for fixo poderá definí-lo em ```page_files=''```

> Como foi o meu caso, não precisei navegar clicando em diferentes menus até chegar no endereço, mas se precisar, também é possível adaptar conforme sua necessidade.

## Configurar as dependências do Selenium

Para permitir realizar o acesso e a navegação pelo navegador através do Selenium se faz necessário baixar **chromedriver_win32.zip**, lembrando que você deverá baixar para o seu navegador em específico caso não seja o Google Chrome. Para mais informações acesse a documentação do [Selenium](https://www.selenium.dev/pt-br/documentation/webdriver/getting_started/install_drivers/)

a) Acessar o endereço https://chromedriver.chromium.org/downloads e baixar o arquivo conforme a versão do seu browser. Para saber qual a versão baixar é simples, abra o Google Chrome e vá em ```Configurações > Sobre o Google Chrome``` e verá a mensagem:

![image](https://user-images.githubusercontent.com/22162514/193193586-c40478bf-1bea-4577-bc68-9e468c0fe11f.png)

b) Descompactar o arquivo **chromedriver_win32.zip** <br>
c) Copiar o seu conteúdo para dentro da pasta raiz do Python ```C:\WebScraping-Selenium-Python\selenium_webdriver\```

> Outro passo importante é criar um path em variáveis de ambiente, também é simples, só seguir os próximos passos.

d) Clicar com botão direito em **Este Computador / Meu Computador** <br>
e) Clicar em Configurações avançadas do sistema <br>
f) Clicar em **Variáveis de Ambiente** <br>
g) Selecionar **Path** e clicar em Editar <br>
h) Clicar em Novo <br>
i) Adicionar o caminho onde colocou o **chromedriver.exe** <br>

## Bibliotecas utilizadas

```os.path```
```pathlib```
```selenium```
```time```
```ftplib```
```sys```
```os```
```pyodbc```
```datetime```
```bs4```
```zipfile```
```pyinstaller```

## Etapas implementadas

- [x] Acessar o site e realizar o login
- [x] Direcionar até o destino onde estão os arquivos a serem baixados
- [x] Adicionar condição para baixar os arquivos corretos por meio do xPath
- [x] Criar diretório temporário Temp e Duplicados para manipulação dos arquivos
- [x] Validar se a quantidade baixada correponde a quantidade que foi feito download do site
- [x] Descompactar arquivos .ZIP
- [x] Mover arquivos para a pasta de destino C:\Concessionária\Retorno\
- [x] Registrar log dos arquivos a serem copiados para o servidor
- [x] Copiar arquivos para o servidor
- [x] Realizar também uma cópia para a pasta C:\Concessionária\Retorno\Baixados\
- [x] Excluir arquivos que foram copiados com sucesso da pasta C:\Concessionária\Retorno\
- [x] Adaptar para que seja possível executar para mais de um usuário
- [x] Enviar log via E-mail

## Gerar executável

Primeiro será necessário instalar a biblioteca PyInstaller que será responsável por gerar esse arquivo .exe: <br>
```
pip install PyInstaller
```
Agora, só acessar a raiz de seu projeto e executar o seguinte comando:
```
pyinstaller --onefile --noconsole automatizacao_edp.py
```

Se utiliza importar alguma biblioteca sua ou de terceiros será necessário utilizar **--paths=../** para gerar o executável.

```
pyinstaller --onefile --noconsole --paths=../ automatizacao_edp.py
```

> Lembrando que automatizacao_edp.py é o nome do arquivo principal, por isso, é informado na hora de gerar o executável.

# Conclusão

Essa automatização se fez necessária com a grande demanda de atividades diárias que foram surgindo, a ncessidade de diariamente ter que acessar um determinado site e baixar os arquivos de retorno que não poderiam deixar de serem lidos. Fazer esse processo manualmente acaba expondo a erros e consequentemente no disperdício de recursos. Além disso, conversa diretamente com o clientecentrismo, quando podemos diminuir as falhas e agilizar os processos de baixas de suas mensalidades evitando qualquer desconforto no bloqueio dos serviços.
