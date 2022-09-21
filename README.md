![banner ponto py](https://user-images.githubusercontent.com/108769169/190526731-c3f5f358-3294-4701-b0f0-85e26e8d63e9.png)

<br id="topo">
<p align="center">
    <a href="#sobre">Projeto</a>  |
    <a href="#backlogs">Backlogs do produto</a>  |
    <a href="#entrega">Entrega das Sprints</a>  |
    <a href="#configurando">Configurando o ambiente</a>  |
    <a href="#tecnologias">Tecnologias</a>  |
    <a href="#equipe">Equipe</a>
</p>

<span id="sobre">

## :white_medium_square: O Projeto
<br></br>
![obj ponto py](https://user-images.githubusercontent.com/108769169/190527313-125dad18-9fc1-4ba7-9da6-49e733b80377.png)

> Projeto baseado na metodologia ágil SCRUM.

<span id="backlogs">

## :white_medium_square: Backlog do produto

|  **ID**   | **COMO UM** |  **EU QUERO**  | **PARA** | **PRIORIDADE** | **SPRINT** | **STATUS** |
|-------------|-----------------------|-------------------------|-------------------------|---------------------|----------------|-------------------------|
|  01  | Usuário | Criar uma conta | Acessar o sistema e fazer as avaliações | Imprescindível | 1 | **Entregue** |
|  02  | Usuário | Logar na minha conta já criada | Acessar os sistema e fazer as avalizações | Imprescindível | 1 | **Entregue** |
|  03  | Administrador | Criar/salvar perfis para mim e para os meus colegas de time | Poder criar times e adicionar os membros | Imprescindível | 2 | A iniciar |
|  04  | Administrador | Editar e excluir perfis | Erros, alterações e manipulação de dados | Importante | 2 | A iniciar |
|  05  | Líder de Time | Criar um time para mim e meus colegas de trabalho | Organizar a minha equipe dentro de um time | Imprescindível | 1 | **Entregue** |
|  06  | Líder de Time | Editar e excluir times | Erros e alterações | Importante | 2 | A iniciar |
|  07  | Líder de Time | Criar, editar e salvar as sprints | Organizar o cronograma  da equipe | Imprescindível | 2 | A iniciar |
|  08  | Usuário | Realizar a minha avaliação e dos meus colegas de equipe | Completar a avaliação 360° | Imprescindível | 2 | A iniciar |
|  09  | Usuário | Ver os resultados das médias das minhas notas | Ter uma noção de como fui avaliado | Desejável | 3 | A iniciar |
|  10  | Líder de Time | Dashboard com informações sobre as sprints, meus colegas de time e minhas avalizações | Melhor visibilidade sobre o time e as sprints | Desejável | 4 | A iniciar |
|  11  | Usuário | Gráficos de desempenho das minhas notas na dashboard | Uma noção individual de performance | Desejável | 4 | A iniciar |
|  12  | Administrador | Atribuir perfis à uma função especial (Instrutor, Líder técnico, etc) | Ter acesso a mais informações e avaliações adicionais | Imprescindível | 3 | A iniciar |

<span id="entrega">

## :white_medium_square: Entrega das Sprints

| **SPRINT** | **PERÍODO**| **O QUE SERÁ ENTREGUE** | **BACKLOG DAS SPRINTS** |
|:-------------:|:-----------------------:|:-------------------------:|:-------------------------:|
|  01  | 29/08 a 18/09 | Criação de cadastro, login na conta criada e criação de times | [Sprint 1](https://github.com/pontopython/api-bd1/wiki/Backlog-da-Sprint-1)
|  02  | 19/09 a 09/10 |
|  03  | 17/10 a 06/11 |
|  04  | 07/11 a 27/11 |

<span id="configurando">

## :white_medium_square: Configurando o ambiente e executando o projeto

Atualize o `pip` e o `virtualenv`:
```sh
python -m pip install --upgrade pip virtualenv
```

Crie um virtual environment numa pasta dentro do próprio projeto (`.venv`):
```sh
python -m virtualenv .venv --prompt="api-bd1"
```

Ative o virtual environment:
```sh
source .venv/bin/activate
```

Com o virtual environment ativado instale as dependências do projeto:
```sh
pip install -r requirements.txt
```

Caso necessário crie a pasta `data` e dentro crie um arquivo `users.txt` vazio.

<span id="tecnologias">

## :white_medium_square: Tecnologias
![tec ponto py](https://user-images.githubusercontent.com/108769169/190526798-76a1088a-017a-4a18-9c7c-d77aac51266a.png)
    
- **Back-end:** Python.
- **Ferramentas:** Git, Github, Canva, Visual Studio Code, Microsoft Teams.

<span id="equipe">

## :white_medium_square: Equipe
![time ponto py](https://user-images.githubusercontent.com/108769169/190527834-12083ff1-5dc5-4638-9f26-47056c5833cf.png)

    
|    Função     | Nome                                  |                                                                                                                                                      LinkedIn & GitHub                                                                                                                                                      |
| :-----------: | :------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Scrum Master | Nicole Souza           |     [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/nicolem-souza/) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/NicSouza)              |
| Product Owner | Alec Rondel           |     [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](http://linkedin.com/in/alecrondel) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/aleclr)              |
| Developer| Alessandra Moreira           |     [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/alessandra-moreira-780b76183) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/Alemoreira-00)              |
| Developer| Evelyn Costa           |     [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/evelynccosta) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/evellyncs)              |
| Developer| Johnny Dutra           |     [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/jnydutra) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/jnydutra)              |
| Developer| Karolina Flores           |     [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/karolina-maria-flores-louren%C3%A7o-426b86169/) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/karolina-flores)              |
| Developer| Larissa Fernanda           |     [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/larissa-reis-693568250/) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/larissa-fernanda)
| Developer| Markus Gomes        |     [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/markus-gomes-013b76250) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/markusgomes)


→ [Voltar ao topo](#topo)
