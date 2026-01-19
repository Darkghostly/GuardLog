# 🛡️ GuardLog: Monitor de Autenticação (Security Log Analysis)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

## 🎯 Sobre o Projeto
O GuardLog é um projeto educacional em Python voltado para análise de logs de autenticação com foco em detecção de ataques de força bruta (Brute Force).

O script processa arquivos de log de autenticação (como auth.log), identifica padrões suspeitos de falhas de login utilizando expressões regulares e gera alertas quando um limite de segurança é ultrapassado dentro de uma janela de tempo definida.

Este projeto simula conceitos utilizados em monitoramento de segurança, Blue Team e SIEM, com foco em aprendizado prático e progressivo.

## ⚙️ Arquitetura do Sistema
O projeto foi desenvolvido de forma modular, facilitando manutenção e evolução.

### 🔧 1. Arquivo de Configuração (config.py)

Responsável por centralizar os parâmetros do sistema.

Variáveis configuráveis:

LOG_FILE: caminho do arquivo de log analisado

MAX_FAILED_ATTEMPTS: limite de falhas antes do alerta

TIME_WINDOW_SECONDS: intervalo de tempo analisado

FAILED_LOGINS_PATTERNS: padrões Regex de falha de autenticação


### 2. Monitoramento e Análise (monitor.py)

Avaliação de ataques por volume dentro de uma janela de tempo

O script percorre o arquivo de log linha por linha.

Utiliza a biblioteca re do Python para buscar padrões específicos de erro (ex: Failed password ou invalid user) definidos no arquivo de configuração.

Gerencia um contador em tempo real das ocorrências detectadas.

### 3. Alerta de Segurança
Compara o total de falhas encontradas com o limite de segurança.

Emite um alerta visual no terminal caso a ameaça seja confirmada.

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.

* **Módulo Nativo:** re (Expressões Regulares) para análise de texto.

* **Módulo Nativo:** datetime para registro de eventos.

## 🚀 Como Executar
### Pré-requisitos
Certifique-se de ter o Python instalado. Não são necessárias bibliotecas externas.

### Execução
Clone o repositório:

```Bash
git clone https://github.com/seu-usuario/guardlog.git

```

Ajuste as configurações no arquivo config.py se necessário (como o caminho para o seu auth.log).

Inicie o monitor:

```Bash
python monitor.py

```

## 💻 Exemplo de Código
Abaixo, a lógica utilizada para filtrar as tentativas de login falhas através dos logs:

```Python
for line in file:
    for pattern in FAILED_LOGINS_PATTERNS:
        if re.search(pattern, line):
            failed_attempts.append(timestamp)
            break

```
(Trecho extraído do arquivo monitor.py)

## 📊 Exemplo de Log Processado
O sistema é capaz de identificar entradas como estas presentes no auth.log:

2026-01-18 14:01:11 Failed password for invalid user admin from 192.168.0.10 port 22 <br>
2026-01-18 14:01:12 Failed password for root from 192.168.0.10 port 22

## 👤 Autor
**Gustavo Bueno da Silva**


* [LinkedIn](https://www.linkedin.com/in/gustavo-bueno-da-silva-797292324)
* [GitHub](https://github.com/Darkghostly)

---

