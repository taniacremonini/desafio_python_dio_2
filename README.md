# 💰 Sistema Bancário em Python

Este projeto simula um sistema bancário simples para fins didáticos, permitindo ao usuário realizar operações básicas como **depósitos**, **saques**, **visualização de extrato**, **criação de usuários**, **criação de contas correntes** e **listagem de contas**.

---

## 🚀 Funcionalidades

- **[d] Depositar**: Realiza um depósito no saldo da conta.
- **[s] Sacar**: Realiza um saque do saldo, respeitando o limite diário e por transação.
- **[e] Extrato**: Exibe o histórico de transações com data e hora.
- **[u] Criar usuário**: Cadastra um novo cliente com CPF, nome, data de nascimento e endereço.
- **[c] Criar conta**: Cria uma conta bancária vinculada a um usuário existente.
- **[lc] Listar contas**: Lista todas as contas criadas com seus dados.
- **[q] Sair**: Encerra o sistema.

---

## 🧑‍💻 Como Executar

1. Certifique-se de ter o **Python 3.x** instalado.
2. Salve o código em um arquivo chamado `sistema_bancario.py`.
3. Execute o programa no terminal:

```bash
python sistema_bancario.py
🗂️ Estrutura do Sistema
depositar(): Função que adiciona saldo e registra no extrato.

sacar(): Função que permite saque com verificação de limite e quantidade.

exibir_extrato(): Mostra todas as movimentações realizadas.

criar_usuario(): Registra novos usuários por CPF único.

criar_conta(): Cria uma conta associada a um usuário.

listar_contas(): Exibe todas as contas criadas e seus titulares.

Menu principal com loop while True.

✅ Requisitos
Python 3.x instalado.

Bibliotecas padrão: datetime e textwrap.

📌 Observações
Cada CPF pode estar vinculado a múltiplas contas, mas não pode ser repetido no cadastro de usuário.

Os dados são armazenados em memória (listas), portanto são perdidos ao encerrar o programa.

O extrato exibe data e hora de cada operação.

🛠️ Melhorias Futuras
Autenticação por CPF para entrada no sistema.

Armazenamento dos dados em arquivo ou banco de dados.

Exportação do extrato para .txt ou .pdf.

Interface gráfica com Tkinter ou PyQt.

Operações com múltiplas contas por usuário.



📄 Licença
Este projeto é de uso educacional e livre para aprendizado e testes pessoais.

