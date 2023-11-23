# pytest
Introdução ao Pytest

criação do ambiente virtual venv

``python -m venv .venv``

atualizar pip

``pip install --upgrade pip``

instalar o pytest

``pip install pytest``

rodar o pytest

``pytest``

todos os arquivos de teste precisam iniciar ou finalizar com test_ ou _test assim como seus metodos ou funções.

para mostrar os testes verbosos use a flag -v

O teste só pode ter um assert.

Prática:

Brincadeira -> BuzzFizz ou Queijo, Goiabada, Romeu e Julieta.

Queijo = número multiplo de 3.
Goiabada = número multiplo de 5.
Romeu e Julieta = número multiplo de 3 e 5.


O teste é formado por três etapas(ou quatro):

GWT:
- Given
- When
- Then

Brincadeira vai ser um SUT - System Under Test

Erro!
Avaliar o E

ERROS DE ESTRUTURA
O primeiro erro é causado pelo modulo (dunder init) - organizacao de diretorios
O segundo erro é porque ainda não foi criada a função brincadeira - erro de chamada

ERROS DE TESTE
Assert errors.

Atenção aos outputs do terminal. Ele mostra exatamente aonde o erro acontece.

Ao verificar cada teste, o pytest passa por todos antes de parar.
Se quisermos parar quando o primeiro erro acontece é só adicionar a flag -x
Isso é útil quando temos vários testes e testes demorados. Interromper logo no primeiro erro pode poupar tempo.

Podemos também chamar o debugger com a flag --pdb
Usar a flag -k "palavra_inclusa_no_teste" para rodar somente testes com aquela palavra.
Flag -s mostra o print() gerado do código. (debugando com prints!?)


Respostas do resumo:

. - Passou
F - Falhou
x - Falha esperada
X - Falha esperada, mas não ocorreu
s - Saltou


Resultado dos testes

Como salvar os reports?

``pytest --junitxml report.xml``

Framework de teste em java. Padrão de teste do mercado.

Mark - Marcações

Smoke test! Onde tem fumaça tem fogo! Tags para selecionar os testes mais importantes.

criando tags para marcar os testes.

``@mark."nome_da_tag"``

rodando os testes marcados:

``pytest -m goiabada``

rodando os testes que não estão marcados:

``pytest -m "not goiabada"``

Agrupar testes que fazem sentido juntos (mark.windows, mark.linux, mark.sql, etc)

Tags embutidas

- @mark.skip - salta o teste
- @mark.skipif - salta um teste com condição (flag -rs mostra motivo)
- @mark.xfail - é esperado que falhe
- @mark.usefixture - 
- @mark.parametrize - parametrizar testes

Parametrizar!!

Executa o mesmo teste várias vezes com parâmetros diferentes.


FIXTURES!!!

Apenas o básico, introdução. Conteúdo muito extenso.

Um fixture de teste de software configura um sistema para o processo de teste de software ao inicializá-lo, satisfazendo assim quaisquer pré-condições que o sistema possa ter. Por exemplo, framework web Ruby on Rails usa YAML para inicializar um banco de dados com parâmetros conhecidos antes de executar um teste. Isso permite que os testes sejam repetidos, o que é um dos principais recursos de uma estrutura de teste eficaz.

``pytest --fixtures``

é importante para o teste mas não faz parte do contexto SUT

é possível criar suas próprias fixtures!