# 🧪 QA - Testes Automatizados de Calculadora

<div align="center">

[![Testes QA](https://github.com/gusjmo/qa-calculadora/actions/workflows/testes.yml/badge.svg)](https://github.com/gusjmo/qa-calculadora/actions/workflows/testes.yml)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

![Status](https://img.shields.io/badge/Status-Ativo-brightgreen?style=flat-square)
![Tipo](https://img.shields.io/badge/Tipo-Portf%C3%B3lio%20QA-purple?style=flat-square)

</div>

---

## 📖 Sobre o Projeto

Projeto de **testes automatizados** desenvolvido com **Pytest** para demonstrar habilidades em **Quality Assurance (QA)**.

O projeto testa uma calculadora com as 4 operações básicas, cobrindo cenários positivos, negativos e casos de borda — simulando um ambiente real de testes de software.

---

## ✅ O que é testado

| Operação | Cenários Cobertos |
|----------|-------------------|
| ➕ Adição | Positivos, negativos, zero |
| ➖ Subtração | Positivos, negativos, zero |
| ✖️ Multiplicação | Positivos, negativos, zero |
| ➗ Divisão | Positivos, divisão por zero (exceção) |

---

## 🛠️ Tecnologias Utilizadas

- **Python 3** — Linguagem principal
- **Pytest** — Framework de testes
- **GitHub Actions** — CI/CD para execução automática dos testes a cada push

---

## 📁 Estrutura do Projeto

```
qa-calculadora/
├── calculadora.py          # Lógica da calculadora
├── test_calculadora.py     # Testes automatizados com Pytest
├── requirements.txt        # Dependências do projeto
└── .github/
    └── workflows/
        └── testes.yml      # Pipeline CI/CD (GitHub Actions)
```

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.x instalado

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/gusjmo/qa-calculadora.git

# 2. Acesse a pasta
cd qa-calculadora

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute os testes
pytest test_calculadora.py -v
```

### Exemplo de saída esperada

```
test_calculadora.py::test_adicao PASSED
test_calculadora.py::test_subtracao PASSED
test_calculadora.py::test_multiplicacao PASSED
test_calculadora.py::test_divisao PASSED
test_calculadora.py::test_divisao_por_zero PASSED
```

---

## ⚙️ CI/CD com GitHub Actions

Este projeto conta com uma pipeline de **integração contínua** configurada via GitHub Actions que:

- Executa todos os testes automaticamente a cada `push` ou `pull request`
- Garante que nenhuma alteração quebre o código existente
- Exibe o badge de status dos testes no topo do README

---

## 📚 Aprendizados

- Escrita de testes unitários com Pytest
- Tratamento de exceções em testes (ex: divisão por zero)
- Configuração de pipeline CI/CD com GitHub Actions
- Boas práticas de QA: nomenclatura, cobertura e organização de testes

---

## 👨‍💻 Autor

**Gustavo Juvencio** — [@gusjmo](https://github.com/gusjmo)

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gustavo-juvencio/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/gusjmo)

---

<div align="center">
  <sub>Projeto de portfólio — QA & Automação de Testes | 2025</sub>
</div>
