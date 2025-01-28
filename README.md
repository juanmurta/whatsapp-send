# 💻 automacao-whatsapp

# 📕 Descrição
Este projeto utiliza a biblioteca Selenium para realizar automação no envio de mensagens e arquivos pelo WhatsApp Web. A aplicação carrega uma planilha Excel contendo os dados necessários (nome, telefone, mensagem e arquivo), formata as mensagens personalizadas para cada destinatário e faz o envio de forma automatizada. Além disso, trata possíveis erros, como números inválidos, e realiza o envio de arquivos quando especificado.

# ☕ Como Usar
1. **Pré-requisitos:**
   - Certifique-se de ter o Google Chrome instalado.
   - Instale a biblioteca Selenium: `pip install selenium`.
   - Instale a biblioteca pandas: `pip install pandas`.
   - Faça o download do driver do ChromeDriver compatível com sua versão do navegador e adicione-o ao PATH do sistema.
   - Configure um perfil do Chrome para ser usado com o Selenium.

2. **Configurações do Projeto:**
   - Ajuste o caminho do perfil do navegador na linha: 
     ```python
     options.add_argument(r'user-data-dir=C:\Users\User\AppData\Local\Google\Chrome\User Data\Profile Selenium')
     ```
   - Certifique-se de que o arquivo Excel (Envios.xlsx) está no caminho correto. O arquivo deve conter as colunas:
     - `nome`: Nome do destinatário.
     - `telefone`: Número do WhatsApp com o código do país e DDD (ex.: 5511999999999).
     - `mensagem`: Mensagem a ser enviada (pode conter "fulano" para personalização).
     - `arquivo`: Nome do arquivo a ser enviado ou "N" caso não haja arquivo.
   - Ajuste o caminho base do arquivo Excel:
     ```python
     tabela = pd.read_excel(r'E:\Python\python\Impressionador\Web-Scraping Selenium\Arquivos\Envios.xlsx')
     ```

3. **Execução:**
   - Execute o script Python e mantenha o computador sem interação manual durante o processo.
   - Certifique-se de que o WhatsApp Web está carregado corretamente no navegador antes do envio.

# Contribuindo para automacao-whatsapp
1. Para contribuir com automacao-whatsapp, siga estas etapas:
2. Bifurque este repositório.
3. Crie um branch: `git checkout -b <nome_branch>`.
4. Faça suas alterações e confirme-as: `git commit -m '<mensagem_commit>'`.
5. Envie para o branch original: `git push origin automacao-whatsapp/<local>`.
6. Crie a solicitação de pull.

Como alternativa, consulte a documentação do GitHub em [como criar uma solicitação pull](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).
