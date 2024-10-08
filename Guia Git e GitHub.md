
Configurações de usuário

	$ git config --global user.name "[nome]"
	Configura o nome que você quer ligado as suas transações de
	commit
	$ git config --global user.email "[endereco-de-email]"
	Configura o email que você quer ligado as suas transações de commit
	$ git config --global color.ui auto
	Configura o email que você quer ligado as suas transações de commit

Crie repositório

	$ git init [nome-do-projeto]
	Cria um novo repositório local com um nome específico
	$ git clone [url]
	Baixa um projeto e seu histórico de versão inteiro

Fazendo mudanças

	$ git status
	Lista todos os arquivos novos ou modificados para serem commitados
	$ git add [arquivo]
	Faz o snapshot de um arquivo na preparação para versionamento
	$ git reset [arquivo]
	Deseleciona o arquivo, mas preserva seu conteúdo
	$ git diff
	Mostra diferenças no arquivo que não foram realizadas
	$ git diff --staged
	Mostra a diferença entre arquivos selecionados e a suas últimas
	versões
	$ git commit -m "[mensagem descritiva]"
	Grava o snapshot permanentemente do arquivo no histórico de versão

Mudanças em grupo

	$ git branch
	Lista todos os branches locais no repositório atual
	$ git branch [nome-do-branch]
	Cria um novo branch
	$ git checkout [nome-do-branch]
	Muda para o branch específico e atualiza o diretório de trabalho
	$ git merge [branch]
	Combina o histórico do branch específico com o branch atual
	$ git branch -d [nome-do-branch]
	Exclui o branch específico

Mude e remova os arquivos versionados

	$ git rm --cached [arquivo]
	Remove o arquivo do controle de versão mas preserva o arquivo
	localmente
	$ git rm [arquivo]
	Remove o arquivo do diretório de trabalho e o seleciona para remoção
	$ git mv [arquivo-original] [arquivo-renomeado]
	Muda o nome do arquivo e o seleciona para o commit

Exclua arquivos e diretórios temporários

	*.log
	build/
	temp-*
	Um arquivo de texto chamado `.gitignore` suprime o versionamento
	acidental de arquivos e diretórios correspondentes aos padrões
	específicados
	
	$ git ls-files --other --ignored --exclude-standard
	Lista todos os arquivos ignorados neste projeto


Salve fragmentos

	$ git stash
	Armazena temporariamente todos os arquivos rastreados modificados
	$ git stash list
	Lista todos os conjuntos de alterações em stash
	$ git stash pop
	Restaura os arquivos recentes em stash
	$ git stash drop
	Descarta os conjuntos de alterações mais recentes em stash

Revise históricos

	$ git log
	Lista o histórico de versões para o branch atual
	$ git log --follow [arquivo]
	Lista o histórico de versões para um arquivo, incluindo mudanças de
	nome
	$ git diff [primerio-branch]...[segundo-branch]
	Mostra a diferença de conteúdo entre dois branches
	$ git show [commit]
	Retorna mudanças de metadata e conteúdo para o commit especificado
	$ git log --oneline
	Retorna um resumo dos commits
	$ git log --stat
	Mostra um resumo de arquivos alterados, com o número de linhas adicionadas e removidas
	

Desfaça Commits

	$ git reset [commit]
	Desfaz todos os commits depois de `[commit]`, preservando
	mudanças locais
	$ git reset --hard [commit]
	Descarta todo histórico e mudanças para o commit especificado

Sincronize mudanças

	$ git fetch [marcador]
	Baixe todo o histórico de um marcador de repositório
	$ git merge [marcador]/[branch]
	Combina o marcador do branch no branch local
	$ git push [alias] [branch]
	Envia todos os commits do branch local para o GitHub
	$ git pull
	Baixa o histórico e incorpora as mudanças


# Notas

Adicionando todas as alterações no commit

	git add . 


Ignorar arquivos no git, deve-se criar um arquivo .gitignore com o nome dos arquivos que devem ser ignorados e usar tmp/


Tem como fazer o commit já com o add, usando o -a

	$ git commit -a -m "Inserindo titulo e diminuindo tamanho da pagina"

