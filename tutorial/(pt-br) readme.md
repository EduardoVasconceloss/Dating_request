Sejam bem-vindos, hoje irei mostrar para vocês como fazer um programa para pedir alguém em namoro.

Para abrir o programa, abra o terminal e digite "python3 app.py".

Obs: O criador do programa é o: @professorlucianoz
Eu apenas estou criando o projeto com as mudanças que me agradam e ensinando a vocês o passo a passo.

Atenção: Este programa foi feito utilizando a linguagem Python, então se certifique que o Python esteja instalado no seu computador antes de começar a codar.

1° passo: devemos criar uma nova pasta para o preojeto e abrir essa pasta em uma IDE de sua preferência (Utilizei VsCode).

2° passo: Devemos instalar duas ferramentas para criar um ambiente virtual, a primeira é o "Pipenv", esta ferramenta é necessária para conseguirmos ter acesso ao Pyside6, que é a segunda ferramenta que iremos precisar. O PySide é necessário para criarmos o ambiente virtual que eu citei anteriormente.

3° passo: Abra o terminal do VsCode e digite "pip3 install pipenv"; logo após o Pipenv ser instalado, digite "pipenv install pyside6". Ao finalizar a instalação, dois arquivos irão aparecer na sua pasta "Pipfile" e "Pipfile.lock"; um ambiente virtual também será criado na sua pasta e a biblioteca PySide6 será instalada.

4° passo: Antes de continuar com os passos seguintes, você deve procurar, no terminal, a localização do seu ambiente virtual. A localização aparece logo abaixo da linha "Successfully created virtual enviroment!", irei disponibilizar um print para melhor orientação. Após encontrar a localização do ambiente virtual, você deve copiar, colar e salvar em algum lugar, pode ser o bloco de notas.

5° passo: Vamos entrar no nosso ambiente virtual, para isso, digite "pipenv shell".

6° passo: No terminal, digite "cd 'localização do seu ambiente virtual'", depois digite "dir". Após isso, o terminal irá te mostrar diversas pastas, nós precisamos entrar na pasta "Scripts", então, digite "cd Scripts" e depois digite "dir" novamente. Agora, devem aparecer vários arquivos no seu terminal, mas não se preocupe, utilizaremos apenas um. Digite "pyside6-designer", uma nova janela será aberta no seu computador, esse é o programa "Qt Designer" e nós vamos utilizá-lo para criar o design do nosso programa.

7° passo: Para tornar nossa vida mais fácil, vamos criar um diretório para abrir o Qt Designer. Para isso, copie o diretório do seu ambiente virtual, cole no terminal e adicione o seguinte: "\Scripts\pyside6-designer". Agora, toda vez que você quiser abrir o Qt Designer, você pode ir no terminal e escrever: "C:\Users\cdu_v\.virtualenvs\Dating_request-uw2VL0Xs\Scripts\pyside6-designer"

8° passo: Abra o Qt Designer, selecione a opção "Main Window" e clique em "Create". Agora você pode começar a criar o layout do seu programa como bem quiser, mas caso essa seja sua primeira vez utilizando essa ferramenta, você pode continuar seguindo o passo a passo.

9° passo: Vamos selecionar as dimensões da janela do nosso programa, no canto direito você pode ver as propriedades da sua MainWindow, para esclarecer melhor, as propriedades tem o fundo amarelo, lá você pode encontrar as opções "Width: 800" e "Height: 600", vamos mudar as dimensões para "Width: 462" e "Height: 450".

10° passo: No parte esquerda, vemos várias opções de ferramentas, nós vamos precisar usar a ferramenta "label". Arraste o label para a MainWindow e mude o nome do label para um nome de sua escolha. Depois disso, você pode escrever qualquer mensagem, eu escrevi "Você quer namorar comigo?".

11° passo: Agora vamos alinhar o texto do nosso label ao centro da janela. Clique na área do label e novamente, ao lado direito, vá em propriedades e procure a seção "alignment".  Na propriedade "Horizontal" mude para a opção "AlignHCenter".

12° passo: Vá nas ferramentas, no canto esquerdo, e procure a ferramenta "Frame", você deve arrastar dois frames para sua MainWindow. Para o layout ficar agradável, eu recomendo você alinhar os dois frames no centro da MainWindow e depois, alinhar um frame a esquerda e outro a direita. Depois de alinhar os frames, procure pela ferramenta "Push Button" e arraste dois botões para os frames na MainWindow. Para alinhar os botões nos frames, faça o seguinte, clique com o botão direito na área do frame, deixe o cursor do mouse em cima de "Lay Out" e marque a opção "Lay Out Horizontally". Agora, podemos mudar o texto que está dentro dos botões para "Sim" e "Não", eu também recomendo mudar os nomes dos objetos "frame" e "push button" no canto superior direito, futuramente vamos precisar que os dois frames e os dois butões estejam diferenciados por nome. Para finalizar esse passo, vamos retirar a borda do frame, e para isso, clique na área do frame e procure nas propriedades a opção "frameShape" e mude seu estado para "NoFrame", repita o mesmo processo para o outro frame.

13° passo: É hora de pôr a mão na massa! No canto superior direito, clique com o botão direito em "centralwidget" e selecione a opção "Change styleSheet...", uma pequena janela irá surgir. Nessa janela que surgiu, podemos mudar algumas propriedades dos widgets com alguns comandos. A princípio, vamos adicionar uma cor de fundo para nossa MainWindow, escreva "QWidget#centralwidget{ background-color: }", agora clique em "Add Gradient" e selecione a opção "Wood" e escolha as cores que você deseja. Caso esteja indeciso você pode utilizar as mesmas cores que eu escolhi, basta copiar e colar esse código no seu "Edit Style Sheet": 

QWidget#centralwidget{

    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 138, 173, 255), stop:0.55 rgba(235, 169, 221, 255), stop:0.98 rgba(214, 159, 195, 255), stop:1 rgba(0, 0, 0, 0))

}

14° passo: Vamos continuar deixando nosso programa mais bonito, agora é hora de mudar o estilo do label, para isso, escreva o seguinte código: 

QLabel#nomeQueVocêSalvou{

    font-size: 35px;

    font-weight: bold;

    color: white;

}

15° passo: Finalizando por agora, vamos estilizar os botões. Escreva o código abaixo, mas lembre-se, você pode mudar algumas coisas para ficar do seu jeito.

QPushButton{

    border: 2px solid white;

    font_size: 20px;

    font-weight: bold;

    color: rgba(255, 138, 173, 255);

    min-height: 45px;

    border-radius: 20px;

    background-color: white;

}

16° passo: Você pode baixar o modelo de coração que eu disponibilizei no repositório ou utilizar outra imagem, quando você for baixar o arquivo, recomendo salvar na pasta do seu projeto. No Qt Designer, adicione um label vazio e mude o nome dele para "coração". Clique na área do label e procure a ferramenta "pixmap" e clique no botão com três pontos "..."; Agora clique no ícone de lápis, depois clique no ícone de folha no canto inferior esquedo e mude o nome do arquivo para "resource", agora é só salvar na pasta do seu projeto. Agora clique no ícone que possui um sinal de "+" em uma pasta e coloque o nome "icons", depois disso, clique no ícone ao lado do que você clicou anteriormente e selecione o arquivo do coração que você baixou. E por fim, clique na ferramente "scaledContents", fica abaixo da ferramenta "pixmap", e aumente o tamanho do seu coração.

17° passo: Salve seu arquivo como "main.ui" e passe o cursor do mouse em cima da opção "Form" e clique na opção "View Python Code" e salve como "ui_main.py".

18° passo: Abra um novo terminal no Vscode e digite o seguinte comando "pyside6-rcc resource.qrc -o resource_rc.py". Um novo arquivo será criado na sua pasta.
