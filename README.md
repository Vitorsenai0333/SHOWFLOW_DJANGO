Trem Flow

O **Trem Flow** é um sistema web que eu desenvolvi com a ideia de simular um e-commerce simples, mas bem organizado. O nome vem daquela pegada mineira mesmo — “trem” pode ser qualquer coisa, e aqui virou o fluxo de vendas do sistema.

A ideia foi criar algo funcional, bonito (modo escuro) e que dê pra evoluir depois pra algo maior.


## O que o sistema faz

Basicamente ele gerencia:

* Clientes
* Produtos
* Pedidos

Tudo isso com interface web e também com acesso via API (JSON).

---

## Tecnologias usadas

* Python
* Django
* Django REST Framework
* SQLite 
* HTML + CSS
* Git / GitHub

---

## ⚙️ Como rodar o projeto

### 1. Clonar

```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd NOME_DA_PASTA
```

---

### 2. Criar o ambiente virtual

```bash
python -m venv venv
```

Ativar no Windows:

```bash
venv\Scripts\activate
```

---

### 3. Instalar dependências

```bash
pip install django djangorestframework
```

---

### 4. Rodar as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

⚠️ IMPORTANTE:  
Se aparecer erro como **"no such table"** ou aviso de **migrations não aplicadas**, rode novamente:

```bash
python manage.py migrate
```

---

### 5. Criar usuário admin

```bash
python manage.py createsuperuser
```

---

### 6. Rodar o servidor

```bash
python manage.py runserver
```

Abrir no navegador:

```
http://127.0.0.1:8000/
```

---

## 🔐 Admin

```
http://127.0.0.1:8000/admin/
```

---

## 🌐 Rotas principais (site)

* `/` → Home (dashboard)
* `/clientes/` → Lista de clientes
* `/produtos/` → Lista de produtos
* `/pedidos/` → Lista de pedidos

---

## Rotas da API (JSON)

Você consegue acessar os dados em formato JSON pelas rotas:

* `/api/clientes/`
* `/api/produtos/`
* `/api/pedidos/`

Ou seja, dá pra consumir esses dados via API normalmente.

---

## Interface

O sistema segue um padrão escuro com:

* Azul escuro (fundo)
* Azul claro (destaques)
* Branco (texto)

A ideia foi deixar algo simples, mas com cara de sistema real.

---

## Ideias futuras

Se eu fosse continuar o projeto, daria pra melhorar com:

* MySQL no lugar do SQLite
* Sistema de login mais completo
* Carrinho de compras
* Integração com pagamento
* Dashboard com gráficos

---

## Sobre mim

Esse projeto foi feito por mim como parte de aprendizado e prática com Django.

---

Licença

Projeto para fins acadêmicos e estudo.
