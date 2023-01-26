Sejam bem-vindos, hoje irei mostrar para vocês como fazer um programa para pedir alguém em namoro. Obs: O criador do programa é o: @professorlucianoz 
Eu apenas estou criando o projeto com as mudanças que me agradam e ensinando a vocês o passo a passo.

Atenção: Este programa foi feito utilizando a linguagem Python, então se certifique que o Python esteja instalado no seu computador antes de começar a codar.

1° passo: devemos criar uma nova pasta para o preojeto e abrir essa pasta em uma IDE de sua preferência (Utilizei VsCode).

2° passo: Devemos instalar duas ferramentas para criar um ambiente virtual, a primeira é o "Pipenv", esta ferramenta é necessária para conseguirmos ter acesso ao Pyside6, que é a segunda ferramenta que iremos precisar. O PySide é necessário para criarmos o ambiente virtual que eu citei anteriormente.

3° passo: Abra o terminal do VsCode e digite "pip3 install pipenv"; logo após o Pipenv ser instalado, digite "pipenv install pyside6". Ao finalizar a instalação, dois arquivos irão aparecer na sua pasta "Pipfile" e "Pipfile.lock"; um ambiente virtual também será criado na sua pasta e a biblioteca PySide6 será instalada.

4° passo: Antes de continuar com os passos seguintes, você deve procurar, no terminal, a localização do seu ambiente virtual. A localização aparece logo abaixo da linha "Successfully created virtual enviroment!", irei disponibilizar um print para melhor orientação. Após encontrar a localização do ambiente virtual, você deve copiar, colar e salvar em algum lugar, pode ser o bloco de notas.

5° passo: Vamos entrar no nosso ambiente virtual, para isso, digite "pipenv shell".

6° passo: No terminal, digite "cd 'localização do seu ambiente virtual'", depois digite "dir". Após isso, o terminal irá te mostrar diversas pastas, nós precisamos entrar na pasta "Scripts", então, digite "cd Scripts" e depois digite "dir" novamente. Agora, devem aparecer vários arquivos no seu terminal, mas não se preocupe, utilizaremos apenas um. Digite "pyside6-designer", uma nova janela será aberta no seu computador, esse é o programa "Qt Designer" e nós vamos utilizá-lo para criar o design do nosso programa.

7° passo: Para tornar nossa vida mais fácil, vamos criar um diretório para abrir o Qt Designer. Para isso, copie o diretório do seu ambiente virtual, cole no terminal e adicione o seguinte: "\Scripts\pyside6-designer". Agora, toda vez que você quiser abrir o Qt Designer, você pode ir no terminal e escrever: "C:\Users\cdu_v\.virtualenvs\Dating_request-uw2VL0Xs\Scripts\pyside6-designer"

8° passo: Abra o Qt Designer