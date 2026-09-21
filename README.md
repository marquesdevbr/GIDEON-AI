# 🤖 GIDEON AI

> Assistente pessoal inteligente desenvolvida em Python, inspirada na GIDEON apresentada em *The Flash*.

**Status:** 🚧 Em desenvolvimento


## 📖 Sobre o projeto

A **GIDEON AI** é um projeto pessoal de assistente virtual desenvolvido em **Python**, criado com o objetivo de explorar a integração entre **inteligência artificial, automação, memória, voz e interação com o computador**.

O projeto utiliza uma arquitetura modular, permitindo que diferentes sistemas e ferramentas sejam desenvolvidos e adicionados de forma independente conforme a GIDEON evolui.

A proposta é transformar a GIDEON em uma assistente pessoal cada vez mais capaz, natural e integrada ao ambiente do usuário.


## 🎬 Inspiração

A GIDEON AI é um projeto **independente**, inspirado na **GIDEON**, uma inteligência artificial fictícia apresentada na série de televisão *The Flash*.

A referência à GIDEON é utilizada como inspiração conceitual para o desenvolvimento deste projeto.

O projeto **não possui vínculo oficial, afiliação, patrocínio ou endosso** por parte da série, seus produtores, estúdios ou demais detentores de direitos relacionados à obra.

A implementação, código e desenvolvimento deste projeto são independentes.


## ✨ Funcionalidades

Entre os recursos atualmente implementados ou em desenvolvimento estão:

- 🧠 Integração com modelos de inteligência artificial via OpenRouter (tool calling funcional)
- 🖥️ Automação de tarefas no computador (abrir programas instalados)
- 🌐 Abertura de websites
- 📂 Criação e manipulação de arquivos e pastas
- 🗑️ Exclusão de arquivos com sistema de confirmação
- 🔧 Sistema modular de ferramentas
- 🔊 Recursos de voz: reconhecimento de fala com detecção de silêncio, síntese de voz via ElevenLabs
- 🎙️ Ativação por palavra-chave ("GIDEON") no modo terminal, com reconhecimento aproximado (fuzzy matching)
- 🖼️ Interface gráfica com PySide6, incluindo entrada de comando por texto conectada à IA
- ⚡ Processamento assíncrono (threading) para manter a interface responsiva durante o processamento da IA
- 💾 Sistema de memória
- 🔐 Sistema de confirmação para ações que exigem maior segurança
- 🛡️ Tratamento de erros de API para evitar que falhas de conexão/créditos derrubem a aplicação
- 🧩 Arquitetura preparada para expansão através de módulos

> A GIDEON continua em desenvolvimento e novas funcionalidades serão adicionadas ao longo do projeto.


## 🧠 Inteligência Artificial

A GIDEON utiliza uma arquitetura baseada em provedores de inteligência artificial, permitindo integrar modelos de linguagem ao sistema.

A IA é utilizada para interpretar solicitações do usuário e, quando necessário, interagir com as ferramentas disponíveis no sistema.

O projeto foi desenvolvido buscando separar a camada de inteligência das demais partes da aplicação, facilitando futuras alterações e expansões.


## 🏗️ Arquitetura

A GIDEON foi organizada de maneira modular para facilitar a manutenção e evolução do projeto.

```text
GIDEON/
├── assets/
├── automation/
├── brain/
├── config/
├── core/
├── database/
├── interface/
├── memory/
├── plugins/
├── security/
├── vision/
├── voice/
├── main.py
├── requirements.txt
└── README.md
````

Cada módulo possui uma responsabilidade específica dentro da aplicação, permitindo que novos sistemas sejam incorporados sem depender de uma estrutura monolítica.


## ⚙️ Tecnologias

* 🐍 Python
* 🧠 Inteligência Artificial
* 🔌 APIs de modelos de linguagem
* 🖥️ Automação de desktop
* 🔊 Síntese e processamento de voz
* 💾 Sistemas de memória e armazenamento
* 🧩 Arquitetura modular
* 🪟 PySide6
* 🔐 Variáveis de ambiente para configurações sensíveis


## 🚀 Instalação

Clone o repositório:

```bash
git clone https://github.com/marquesdevbr/GIDEON-AI.git
```

Entre na pasta do projeto:

```bash
cd GIDEON-AI
```

Instale as dependências:

```bash
pip install -r requirements.txt
```


## 🔐 Configuração

A GIDEON utiliza variáveis de ambiente para armazenar informações sensíveis, como chaves de API.

Crie um arquivo `.env` na raiz do projeto:

```text
GIDEON/
├── .env
├── main.py
├── requirements.txt
└── ...
```

Configure nele as variáveis necessárias para o funcionamento da aplicação.

> ⚠️ O arquivo `.env` não deve ser publicado no GitHub.

Nunca compartilhe ou publique:

* 🔑 Chaves de API
* 🔐 Senhas
* 🪪 Tokens de autenticação
* 📁 Outras informações sensíveis


## ▶️ Execução

Depois de instalar as dependências e configurar o ambiente, execute:

```bash
python main.py
```

A aplicação será inicializada através do arquivo principal.


## 🗺️ Roadmap

### ✅ Concluído

* [x] Estrutura inicial do projeto
* [x] Arquitetura modular
* [x] Integração com inteligência artificial
* [x] Sistema de comandos
* [x] Sistema de ferramentas
* [x] Automação do computador
* [x] Abertura de websites
* [x] Criação de arquivos e pastas
* [x] Sistema de confirmação de ações
* [x] Recursos iniciais de voz
* [x] Tool calling funcionando de ponta a ponta (voz e texto)
* [x] Tratamento de erros de API sem derrubar a aplicação
* [x] Interface gráfica com entrada de comando por texto
* [x] Processamento assíncrono na interface gráfica (sem congelamento)
* [x] Ativação por palavra-chave ("GIDEON") no modo terminal

### 🚧 Em desenvolvimento

* [ ] Aprimorar sistema de memória
* [ ] Adicionar entrada por voz na interface gráfica
* [ ] Adicionar ativação por palavra-chave também na interface gráfica
* [ ] Saudação automática ao abrir a interface gráfica
* [ ] Expandir sistema de visão
* [ ] Desenvolver novos módulos
* [ ] Melhorar interação por voz
* [ ] Tornar a interação mais natural
* [ ] Melhorar gerenciamento de ferramentas

### 🔮 Futuro

* [ ] Criar versões estáveis
* [ ] Expandir capacidades da assistente
* [ ] Desenvolver novos sistemas de automação
* [ ] Melhorar integração entre os módulos


## 🔒 Segurança

A GIDEON possui mecanismos de confirmação para determinadas ações realizadas no computador.

A utilização de variáveis de ambiente também permite manter informações sensíveis separadas do código-fonte.

O arquivo `.env` deve permanecer fora do controle de versão através do `.gitignore`.

> **Nunca publique chaves de API, senhas ou tokens no repositório.**


## 📚 Objetivo do projeto

Além de desenvolver uma assistente pessoal, a GIDEON AI é um projeto de aprendizado e experimentação.

O desenvolvimento permite estudar e aplicar conceitos relacionados a:

* Python
* Inteligência Artificial
* APIs
* Automação
* Arquitetura de software
* Desenvolvimento de interfaces
* Sistemas modulares
* Git e GitHub
* Segurança de aplicações

A ideia é aprender através da construção de um projeto real e evoluí-lo continuamente.


## 👨‍💻 Desenvolvedor

**Gabriel Marques**

Desenvolvedor em formação e criador da GIDEON AI.


## 📄 Licença

Este projeto é disponibilizado para fins de estudo, aprendizado e desenvolvimento pessoal.

A licença e as condições de uso do código podem ser definidas conforme a evolução e publicação do projeto.


> **GIDEON AI — Your personal intelligent assistant.**