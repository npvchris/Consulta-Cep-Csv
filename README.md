Esse código é um aplicativo de consulta de disponibilidade de cabeamento para um CEP específico. Ele permite que o usuário insira um CEP e selecione um tipo de provedor de serviços (Claro, TIM ou Vivo) para verificar se há cabeamento disponível para esse CEP. Ao clicar no botão "Consultar", o programa verifica se o CEP está presente no arquivo CSV correspondente ao provedor selecionado e exibe uma mensagem indicando se o cabeamento está disponível ou não.




Instruções de Instalação e Execução
Este é um aplicativo de consulta de disponibilidade de cabeamento para um determinado CEP, com base em diferentes tipos de provedores de serviços (Claro, TIM, Vivo). Siga as instruções abaixo para instalar e executar o aplicativo em seu sistema.

Pré-requisitos
Python 3.x instalado em seu sistema. Você pode baixar o Python em python.org .
Passos de Instalação
Clone este repositório em sua máquina local usando o seguinte comando:

festa

Copiar código
git clone https://github.com/seuusuario/seurepositorio.git
Substitua seuusuarioe seurepositoriopelos seus detalhes de usuário e repositório do GitHub.

Navegue até o diretório do projeto:

festa

Copiar código
cd seurepositorio
Instale as dependências necessárias usando o pip:


Copiar código
pip install pandas
Executando o Aplicativo
Após concluir a instalação das dependências, execute o aplicativo com o seguinte comando:


Copiar código
python consulta_cep.py
Isso iniciará a interface gráfica do aplicativo de consulta do CEP.

Insira o CEP



Para executar este código, você precisa ter o Python instalado em seu sistema. Se você ainda não tem o Python instalado, pode baixá-lo e encontrá-lo no site oficial: Python.org .

Além disso, você precisará instalar duas bibliotecas Python: pandas e tkinter. Felizmente, o pandas geralmente vem pré-instalado em muitos ambientes Python, mas você pode encontrá-lo usando o pip se necessário. O tkinter também é comumente incluído nas distribuições padrão do Python.

Para instalar o pandas, se necessário, e verificar se você tem o tkinter instalado, você pode usar o seguinte comando em seu terminal ou prompt de comando:


Copiar código: pip install pandas

Depois de ter o Python e as bibliotecas necessárias instaladas, basta salvar o código em um arquivo com a extensão .py, por exemplo, consulta_cep.py. Em seguida, execute o arquivo Python usando o interpretador Python. Você pode fazer isso navegando até o diretório onde o arquivo está localizado em seu terminal ou prompt de comando e escrevendo:

python consulta_cep.py

Isso iniciará a interface gráfica do aplicativo de consulta do CEP e você poderá usá-lo conforme explicado anteriormente. Certifique-se de ter um arquivo CSV para cada provedor de serviços com os dados de CEP necessários, ou então o programa pode não funcionar corretamente.


