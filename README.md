# 🚀 FakePinterest

Aplicação web desenvolvida com **Flask** que simula funcionalidades básicas do Pinterest, permitindo autenticação de usuários, upload de imagens e visualização de conteúdo em um feed.

---

## 📌 Sobre o projeto

O **FakePinterest** foi desenvolvido com o objetivo de aprofundar conhecimentos em desenvolvimento web com Flask, abordando conceitos essenciais como:

* Autenticação de usuários
* Manipulação de banco de dados
* Upload e tratamento de imagens
* Estruturação de aplicações web

---

## 🎯 Funcionalidades

* ✅ Cadastro de usuários com validações
* ✅ Login e logout com autenticação segura
* ✅ Criptografia de senha com hash
* ✅ Upload de imagens no perfil
* ✅ Redimensionamento automático das imagens
* ✅ Feed com imagens de usuários
* ✅ Visualização de perfil
* ✅ Proteção de rotas com autenticação (`login_required`)

---

## 🛠️ Tecnologias utilizadas

### Backend

* Python
* Flask
* Flask-SQLAlchemy
* Flask-Login
* Flask-Bcrypt
* Flask-WTF

### Frontend

* HTML5
* CSS3
* Jinja2

### Banco de Dados

* SQLite (armazenado na pasta `instance/`)

### Outras bibliotecas

* Pillow (processamento de imagens)
* WTForms (validação de formulários)

---

## 📁 Estrutura do projeto

<pre class="overflow-visible! px-0!" data-start="1440" data-end="1790"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>ProjetoFakePinterest/</span><br/><span>│</span><br/><span>├── instance/</span><br/><span>│   └── pinterestfake.db</span><br/><span>│</span><br/><span>├── static/</span><br/><span>│   ├── css/</span><br/><span>│   └── fotos_posts/</span><br/><span>│</span><br/><span>├── templates/</span><br/><span>│   ├── homepage.html</span><br/><span>│   ├── criarconta.html</span><br/><span>│   ├── perfil.html</span><br/><span>│   ├── feed.html</span><br/><span>│   └── navbar.html</span><br/><span>│</span><br/><span>├── __init__.py</span><br/><span>├── models.py</span><br/><span>├── routes.py</span><br/><span>├── forms.py</span><br/><span>│</span><br/><span>├── create_db.py</span><br/><span>├── main.py</span><br/><span>└── requirements.txt</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## ▶️ Como executar o projeto

### 1. Clonar o repositório

<pre class="overflow-visible! px-0!" data-start="1856" data-end="1919"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼs">git</span><span> clone <seu-repositorio></span><br/><span class="ͼs">cd</span><span> fakepinterest</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

### 2. Criar ambiente virtual

<pre class="overflow-visible! px-0!" data-start="1956" data-end="1987"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>python </span><span class="ͼu">-m</span><span> venv venv</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

Ativar:

**Windows**

<pre class="overflow-visible! px-0!" data-start="2010" data-end="2043"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>venv\Scripts\activate</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

**Linux/Mac**

<pre class="overflow-visible! px-0!" data-start="2059" data-end="2095"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼs">source</span><span> venv/bin/activate</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

### 3. Instalar dependências

<pre class="overflow-visible! px-0!" data-start="2131" data-end="2174"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>pip install </span><span class="ͼu">-r</span><span> requirements.txt</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

### 4. Criar o banco de dados

<pre class="overflow-visible! px-0!" data-start="2211" data-end="2242"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>python create_db.py</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

### 5. Executar a aplicação

<pre class="overflow-visible! px-0!" data-start="2277" data-end="2303"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>python main.py</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

### 6. Acessar no navegador

<pre class="overflow-visible! px-0!" data-start="2338" data-end="2367"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>http://127.0.0.1:5000</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## 📸 Interface da aplicação

### 🔐 Tela de Login

* Interface centralizada com validação de credenciais

### 📝 Cadastro de Usuário

* Criação de conta com validação de dados

### 👤 Perfil

* Upload de imagens
* Visualização das fotos do usuário

### 🖼️ Feed

* Exibição de imagens publicadas

---

## 🔒 Segurança implementada

* Hash de senha com `Flask-Bcrypt`
* Proteção de rotas com `Flask-Login`
* Validação de formulários com `Flask-WTF`
* Proteção contra CSRF
* Validação segura de login (sem exposição de dados sensíveis)

---

## 💡 Aprendizados

Durante o desenvolvimento deste projeto foram aplicados conceitos como:

* Estruturação de aplicações Flask
* Integração com banco de dados (ORM)
* Autenticação e gerenciamento de sessão
* Upload e manipulação de arquivos
* Boas práticas de segurança em aplicações web

---

## 🚀 Melhorias futuras

* [ ] Sistema de curtidas
* [ ] Comentários nas imagens
* [ ] Paginação no feed
* [ ] Upload com preview
* [ ] Deploy em produção (Render / Railway)
* [ ] Banco de dados PostgreSQL
* [ ] Exclusão de Imagens

---

## 👨‍💻 Autor

Desenvolvido por **Danilo**

📌 Projeto para fins de estudo e portfólio
