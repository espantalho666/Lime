# Lime - Honeypot FTP

**Lime** é um projeto de honeypot que simula um servidor FTP vulnerável com o objetivo de atrair e monitorar atividades maliciosas. O objetivo principal é capturar tentativas de acesso não autorizado e analisar os métodos e ferramentas utilizados pelos atacantes.

---

## 🚀 Funcionalidades

- **Simulação Realista de FTP**: O Lime imita um servidor FTP comum, incluindo respostas típicas e comportamentos de conexão, para enganar atacantes.
- **Captura de Tentativas de Acesso**: Registra todas as tentativas de login, incluindo informações como IP de origem, tentativas de senha, e comandos executados.
- **Relatórios de Atividade**: Geração de relatórios detalhados sobre as interações dos atacantes, para análise posterior.
- **Monitoramento em Tempo Real**: Logs e monitoramento contínuos para detecção precoce de ataques.

---

## 🔧 Tecnologias Utilizadas

- **Python** - Para o núcleo do honeypot e a simulação do protocolo FTP.
- **SQLite/MySQL** - Para armazenamento de dados de logs e tentativas de acesso.

---

## 📦 Instalação

Siga os passos abaixo para configurar o Lime no seu sistema.

### 1. Clone o repositório

```bash
git clone https://github.com/espantalho666/Lime.git
cd lime
