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

| **COMO UM** |  **EU QUERO**  | **PARA** | **PRIORIDADE** | **SPRINT** | **STATUS** |
|-----------------------|-------------------------|-------------------------|---------------------|----------------|-------------------------|
| Administrador | Criar e armazenar contas | Acessar o sistema | Imprescindível | 1 | **Realizado** |
| Administrador | Editar e excluir contas| Corrigir erros e fazer alterações | Importante | 2 | **Realizado** |
| Usuário | Login/Log-off| Acessar o sistema | Imprescindível | 1 | **Realizado** |
| Líder de time | Criar e armazenar times | Organizar minha equipe | Imprescindível | 1 | **Realizado** |
| Líder de Time | Editar e excluir times  | Corrigir erros e fazer alterações | Importante | 2 | **Realizado** |
| Líder de Time | Criar, editar e salvar as sprints | Organizar o cronograma da equipe | Imprescindível | 3 | **Realizado** |
| Líder de Time | Adicionar usuários ao time | Montar a equipe | Imprescindível | 1 | **Realizado** |
| Usuário | Autoavaliação, avaliação do time e aval. adcionais | Completar a avaliação 360° | Imprescindível | 2 | **Realizado** |
| Usuário | Ver as médias das minhas notas | Noção de performance | Desejável | 2 | **Realizado** |
| Líder de Time | Dashboard com informações de sprints e notas | Visibilidade sobre o time | Desejável | 4 | A iniciar |
| Usuário | Gráficos de desempenho | Noção de performance | Desejável | 4 | A iniciar |
| Desenvolvedor | Aplicar restrições e hierarquia de usuários | Organizar as funcionalidades | Imprescindível | 2 | **Realizado** |

<span id="entrega">

## :white_medium_square: Entrega das Sprints

| **SPRINT** | **PERÍODO**| **O QUE SERÁ ENTREGUE** | **BACKLOG DAS SPRINTS** |
|:-------------:|:-----------------------:|:-------------------------:|:-------------------------:|
|  01  | 29/08 a 18/09 | Criação de cadastro, login na conta criada e criação de times | [Sprint 1](https://github.com/pontopython/api-bd1/wiki/Backlog-da-Sprint-1)
|  02  | 19/09 a 09/10 | Finalização do sistema de cadastro, sistema de avaliação e restrições e permissões dos usuários | [Sprint 2](https://github.com/pontopython/api-bd1/wiki/Backlog-da-Sprint-2)
|  03  | 17/10 a 06/11 |Funcionalidade Turma – ADM, Funcionalidade Sprints - Líder de Turma/ADM, Conta ADM, Correções: Funcionalidade Usuário e Funcionalidade Time | [Sprint 3](https://github.com/pontopython/api-bd1/wiki/Backlog-da-Sprint-3)
|  04  | 07/11 a 27/11 | Visualizações/Dashboards e Finalização da API | [Sprint 4](https://github.com/pontopython/api-bd1/wiki/Backlog-da-Sprint-4)

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
![time ponto py](https://user-images.githubusercontent.com/108769169/199708959-6fcc7464-aa33-48db-82e0-3080cf7635af.png)


    
|    Função     | Nome                                  |                                                                                                                                                      LinkedIn & GitHub                                                                                                                                                      |
| :-----------: | :------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| Scrum Master | Nicole Souza           |     [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/nicolem-souza/) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/NicSouza)              |
| Product Owner | Markus Gomes        |     [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/markus-gomes-013b76250) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/markusgomes)    
| Developer | Alec Rondel           |     [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](http://linkedin.com/in/alecrondel) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/aleclr)              |
| Developer| Alessandra Moreira           |     [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/alessandra-moreira-780b76183) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/Alemoreira-00)              |
| Developer| Evelyn Costa           |     [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/evelynccosta) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/evellyncs)              |
| Developer| Johnny Dutra           |     [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/jnydutra) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/jnydutra)              |
| Developer| Karolina Flores           |     [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/karolina-maria-flores-louren%C3%A7o-426b86169/) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/karolina-flores)              |
| Developer| Larissa Fernanda           |     [![Linkedin Badge](https://img.shields.io/badge/Linkedin-blue?style=flat-square&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/larissa-reis-693568250/) [![GitHub Badge](https://img.shields.io/badge/GitHub-111217?style=flat-square&logo=github&logoColor=white)](https://github.com/larissa-fernanda)


→ [Voltar ao topo](#topo)
