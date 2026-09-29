# fila-atendimento-hands-on-
Sistema Inteligente de Atendimento

Integrantes

-Nome do Integrante 1
-Nome do Integrante 2
-Nome do Integrante 3

Este projeto implementa um Sistema Inteligente de Atendimento
utilizando três tipos de estruturas de fila em Python:

- Fila Clássica (FIFO)
- Fila Circular
- Fila de Prioridade


Perguntas:


1. Por que a ordem de atendimento da fila de prioridade pode ser diferente da ordem da fila clássica?

Na fila clássica, os clientes são atendidos na ordem
em que chegaram. Na fila de prioridade, os clientes são atendidos de
acordo com sua prioridade.
Por isso, um cliente que chegou depois pode ser atendido
antes de outro que chegou anteriormente se possuir uma
prioridade maior.

2. Em quais situações reais uma fila de prioridade seria mais adequada?

Uma fila de prioridade pode ser utilizada em:

* Hospitais;
* Pronto-socorros;
* Centrais de emergência;
* Suporte técnico;
* Sistemas operacionais;
* Gerenciamento de tarefas.

Nesses casos, alguns atendimentos precisam ser
realizados antes de outros.

3.Quais são as vantagens e limitações de uma fila circular?

Entre as vantagens estão o melhor aproveitamento do
espaço disponível e a possibilidade de reutilizar
posições liberadas. Como limitação, a fila possui uma capacidade definida.
Quando está cheia, não é possível adicionar outro
elemento.

4.O que acontece ao tentar inserir um elemento em uma fila circular cheia?

Quando a fila circular está cheia, não existe espaço
disponível para um novo elemento. Nesse caso, o programa informa que a fila está cheia
e não realiza a inserção.
