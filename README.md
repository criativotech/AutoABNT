## 🚀 AutoABNT: Guia de Instalação Rápida

Este script automatiza a configuração de documentos conforme a **NBR 14724:2024** no LibreOffice Writer.

## 🛠️ 1. Onde colocar o script?

O caminho depende do seu sistema operacional e da forma como o LibreOffice foi instalado:

| **Sistema / Instalação** | **Caminho da Pasta de Scripts**                                                    |
| ------------------------ | ---------------------------------------------------------------------------------- |
| **Linux com (Flatpak)**  | `~/.var/app/org.libreoffice.LibreOffice/config/libreoffice/4/user/Scripts/python/` |
| **Linux com (APT)**      | `~/.config/libreoffice/4/user/Scripts/python/`                                     |
| **Windows 10 / 11**      | `%APPDATA%\LibreOffice\4\user\Scripts\python\`                                     |

> **Nota:** Se as pastas `Scripts` e `python` não existirem, crie-as manualmente (respeitando as iniciais maiúsculas/minúsculas).

---

## 🔑 2. Configuração de Segurança

O LibreOffice bloqueia scripts por padrão. Caso o script não funcione, você deve autorizar a pasta:

1. Abra o LibreOffice e vá em **Ferramentas > Opções > Segurança**.
    
2. Clique em **Segurança de Macros > Fontes confiáveis**.
    
3. Clique em **Adicionar** e selecione a pasta onde você colou o script.
    

---

## 🖱️ 3. Criando o Botão de Execução

1. Vá em **Ferramentas > Personalizar > Barra de ferramentas**.
    
2. No campo **Categoria**, selecione **Macros**.
    
3. Navegue em: `Minhas macros > AutoABNT > AplicarFormatacaoABNT`.
    
4. Adicione o comando à sua barra de ferramentas e clique em OK.

Você pode (e deve) clicar em alterar e escolher a opção de ícone para escolher um que seja fácil de identificar na barra de ferramentas.
    

---

## 📖 4. O que a Macro configura?

Ao clicar no botão, o script aplica instantaneamente:

- **Margens**: Superior/Esquerda (3 cm) e Inferior/Direita (2 cm).
    
- **Fonte**: Arial 12 com espaçamento 1,5.
    
- **Parágrafo**: Recuo de primeira linha de **1,25 cm**.
    
- **Títulos**: Remove o recuo para manter o alinhamento à esquerda.
    

---

## ⚠️ 5. Lembretes de Formatação Manual

O script é o "pontapé inicial". Algumas tarefas ainda são manuais:

- **Citações Longas**: Tamanho 10, espaço simples e recuo de 4 cm à esquerda.
    
- **Paginação**: Use a **Quebra Manual** (`Inserir > Mais quebras`) para que a numeração apareça apenas a partir da Introdução.
    
- **Referências**: Alinhar à esquerda e usar espaçamento simples.
    
- **Quebras**: Use `Ctrl + Enter` para iniciar novos elementos (Resumo, Capítulos, etc.).
---

## Autor

-   **chiefmodoc**

[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/K3K01KWCZW)
---
