Este projeto de ciência de dados é uma série que percorre passo a passo o processo de construção de um site de previsão de preços de imóveis. Primeiro, construiremos um modelo usando o sklearn e a regressão linear, utilizando um conjunto de dados de preços de imóveis de Bangalore, Índia, obtido no Kaggle. O segundo passo será criar um servidor em Python com Flask, que utiliza o modelo salvo para responder a requisições HTTP. O terceiro componente é o site, desenvolvido em HTML, CSS e JavaScript, que permite ao usuário inserir informações como área em metros quadrados, quantidade de quartos, etc., e este enviará uma solicitação ao servidor em Flask para obter o preço previsto. Durante a construção do modelo, abordaremos quase todos os conceitos de ciência de dados, como carregamento e limpeza de dados, detecção e remoção de outliers, engenharia de características, redução de dimensionalidade, gridsearchcv para ajuste de hiperparâmetros, validação cruzada k-fold, entre outros. Em termos de tecnologia e ferramentas, este projeto cobre:

Python
Numpy e Pandas para limpeza de dados
Matplotlib para visualização de dados
Sklearn para construção do modelo
Jupyter Notebook, Visual Studio Code e PyCharm como IDE
Python Flask para o servidor HTTP
HTML/CSS/JavaScript para a interface do usuário (UI)
Implantação desta aplicação na nuvem (AWS EC2)
Crie uma instância EC2 usando o console da Amazon e, no grupo de segurança, adicione uma regra para permitir o tráfego HTTP de entrada.

Conecte-se à sua instância com um comando como este:

bash
Copiar código
ssh -i "C:\Users\Viral\.ssh\Banglore.pem" ubuntu@ec2-3-133-88-210.us-east-2.compute.amazonaws.com
Configuração do nginx:

Instale o nginx na instância EC2 com os comandos:
bash
Copiar código
sudo apt-get update
sudo apt-get install nginx
Isso instalará o nginx e o executará automaticamente. Verifique o status do nginx com:
bash
Copiar código
sudo service nginx status
Aqui estão os comandos para iniciar/parar/reiniciar o nginx:
bash
Copiar código
sudo service nginx start
sudo service nginx stop
sudo service nginx restart
Quando você carregar a URL da nuvem no navegador, verá uma mensagem dizendo "Welcome to nginx". Isso significa que o nginx está configurado e em execução.
Agora você precisa copiar todo o seu código para a instância EC2. Você pode fazer isso usando o Git ou copiando os arquivos com o WinSCP. Vamos usar o WinSCP. Baixe o WinSCP aqui: https://winscp.net/eng/download.php

Depois de se conectar à instância EC2 pelo WinSCP (instruções em um vídeo do YouTube), você pode copiar todos os arquivos de código para a pasta /home/ubuntu/. O caminho completo do seu diretório raiz agora é: /home/ubuntu/BangloreHomePrices

Após copiar o código para o servidor EC2, agora podemos configurar o nginx para carregar nosso site de imóveis por padrão. Siga os passos abaixo:

Crie este arquivo /etc/nginx/sites-available/bhp.conf com o seguinte conteúdo:
nginx
Copiar código
server {
    listen 80;
    server_name bhp;
    root /home/ubuntu/BangloreHomePrices/client;
    index app.html;
    location /api/ {
         rewrite ^/api(.*) $1 break;
         proxy_pass http://127.0.0.1:5000;
    }
}
Crie um link simbólico para este arquivo em /etc/nginx/sites-enabled executando este comando:
bash
Copiar código
sudo ln -v -s /etc/nginx/sites-available/bhp.conf
Remova o link simbólico para o arquivo padrão no diretório /etc/nginx/sites-enabled:
bash
Copiar código
sudo unlink default
Reinicie o nginx:
bash
Copiar código
sudo service nginx restart
Agora, instale os pacotes Python e inicie o servidor Flask:

bash
Copiar código
sudo apt-get install python3-pip
sudo pip3 install -r /home/ubuntu/BangloreHomePrices/server/requirements.txt
python3 /home/ubuntu/BangloreHomePrices/client/server.py
O último comando acima indicará que o servidor está em execução na porta 5000.

Agora basta carregar sua URL da nuvem no navegador (no meu caso, era http://ec2-3-133-88-210.us-east-2.compute.amazonaws.com/) e este será um site totalmente funcional em ambiente de produção na nuvem.

Observação: Este projeto foi inspirado em um conjunto de dados de preços de imóveis da Índia, especificamente de Bangalore
