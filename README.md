# 📌 Sistema de Reclamações

## 📖 Sobre o projeto
Este projeto consiste em um backend simples desenvolvido para fins acadêmicos.  
O sistema permite o registro e gerenciamento de reclamações, classificando-as de acordo com seu status e nível de urgência.

Foi desenvolvido utilizando **Python** e o framework **Django**.

---

## 🎯 Tema do sistema
Sistema de gerenciamento de reclamações.

---

## ⚙️ Funcionalidades
- Registrar novas reclamações
- Classificar reclamações como:
  - Respondidas
  - Não respondidas
- Definir nível de urgência:
  - Urgente
  - Não urgente
- Listar reclamações cadastradas
- Atualizar status das reclamações
- Filtrar reclamações por status e urgência

---

## 🌐 Rotas da API

### 🔐 Administração
- `/admin/`  
  Interface administrativa padrão do Django para gerenciamento dos dados.

### 📋 Reclamações
- `/api/reclamacoes/`  
  Lista todas as reclamações e permite cadastro de novas.

- `/api/reclamacoes/abertas`  
  Retorna apenas as reclamações **não respondidas**.

- `/api/reclamacoes/urgentes`  
  Retorna apenas as reclamações marcadas como **urgentes**.

- `/api/reclamacoes/nao_urgentes`  
  Retorna apenas as reclamações marcadas como **não urgentes**.

---

## 💾 Dados armazenados
O sistema armazena informações como:
- Descrição da reclamação
- Status da reclamação (respondida ou não)
- Nível de urgência (urgente ou não urgente)
- Data de criação da reclamação

---

## 🛠️ Tecnologias utilizadas
- Python
- Django

---

## 🚀 Objetivo
Este projeto tem como objetivo servir como prática acadêmica para desenvolvimento de APIs e sistemas backend utilizando Django.
