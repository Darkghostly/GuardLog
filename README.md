# 🛡️ GuardLog: Monitor de Autenticação (Security Log Analysis)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Status](https://img.shields.io/badge/Status-Completed-success)
![License](https://img.shields.io/badge/License-MIT-green)

## 🎯 Sobre o Projeto
O GuardLog é um script de monitoramento de segurança desenvolvido em Python para automatizar a análise de registros de autenticação em servidores Linux.

O foco principal é a detecção preventiva de ataques de Brute Force. O script processa arquivos de log, identifica padrões de falha e alerta o administrador quando o volume de tentativas suspeitas ultrapassa um limite de segurança pré-configurado. Este é um projeto prático focado no pilar de monitoramento contínuo da cultura DevSecOps.

## ⚙️ Arquitetura do Sistema
O projeto foi estruturado para ser modular e de fácil configuração:

### 1. Configuração (config.py)
Centralização de parâmetros globais.

Variáveis configuráveis:

Caminho do arquivo de log (LOG_FILE).

Limite máximo de tentativas falhas antes do alerta (MAX_FAILED_ATTEMPTS).

Definição de padrões de falha via Expressões Regulares (Regex).

### 2. Monitoramento e Análise (monitor.py)
Leitura Eficiente: O script percorre o arquivo de log linha por linha.

Pattern Matching: Utiliza a biblioteca re do Python para buscar padrões específicos de erro (ex: Failed password ou invalid user) definidos no arquivo de configuração.

Contabilização: Gerencia um contador em tempo real das ocorrências detectadas.

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

# Lógica de detecção via Regex
for line in file:
    for pattern in FAILED_LOGINS_PATTERNS:
        if re.search(pattern, line):
            failed_attempts += 1
            break

```
(Trecho extraído do arquivo monitor.py)

## 📊 Exemplo de Log Processado
O sistema é capaz de identificar entradas como estas presentes no auth.log:

Failed password for invalid user admin from 192.168.0.10 port 22

Failed password for root from 192.168.0.10 port 22

## 👤 Autor
**Gustavo Bueno da Silva**


* [LinkedIn](https://www.linkedin.com/in/gustavo-bueno-da-silva-797292324)
* [GitHub](https://github.com/Darkghostly)

---
