# Sistema Bancário Simples em Python

Este é um projeto de sistema bancário rudimentar desenvolvido em Python, focado nas operações básicas de um caixa eletrônico: depósito, saque e exibição de extrato. Foi criado como parte de um estudo ou desafio de programação para consolidar conceitos de lógica de programação, estruturas condicionais (`if/elif/else`), laços de repetição (`while`), tratamento de erros (`try/except`) e manipulação de strings.

## 🚀 Funcionalidades

O sistema oferece as seguintes operações:

* **Depositar (`d`):** Permite ao usuário adicionar um valor positivo ao saldo da conta. O valor é registrado no extrato.
* **Sacar (`s`):** Permite ao usuário retirar um valor da conta, com as seguintes validações:
    * O valor do saque não pode exceder o limite de R$ 500,00 por operação.
    * O valor do saque não pode ser maior que o saldo disponível.
    * Há um limite de 3 saques diários.
    * O valor é registrado no extrato.
* **Extrato (`e`):** Exibe todas as operações de depósito e saque realizadas, juntamente com o saldo atual da conta.
* **Sair (`q`):** Encerra o programa.

## 💻 Como Executar

Para rodar este programa, você precisará ter o Python instalado em sua máquina.

1.  Clone este repositório para o seu ambiente local:
    ```bash
    git clone [https://github.com/SeuUsuario/sistema-bancario-simples-python.git](https://github.com/SeuUsuario/sistema-bancario-simples-python.git)
    ```
    (Lembre-se de substituir `SeuUsuario/sistema-bancario-simples-python.git` pelo caminho real do seu repositório após criá-lo.)

2.  Navegue até a pasta do projeto via terminal ou prompt de comando:
    ```bash
    cd sistema-bancario-simples-python
    ```
    (Ou `cd nome-da-sua-pasta-do-projeto` se você o renomeou)

3.  Execute o arquivo principal (assumindo que o nome do arquivo seja `main.py`):
    ```bash
    python main.py
    ```

## 🛠️ Tecnologias Utilizadas

* **Python 3**

## 🤝 Contribuição

Sinta-se à vontade para explorar o código, sugerir melhorias ou adicionar novas funcionalidades. Forks e Pull Requests são bem-vindos!

## 🧑‍💻 Autor

[Feyki]
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/SeuUsuarioNoGitHub)

---
