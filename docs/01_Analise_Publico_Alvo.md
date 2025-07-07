# 01 - Análise e Planejamento do Projeto de Automação de E-commerce

Nesta seção, detalharemos o problema a ser resolvido, os objetivos que a automação visa alcançar e a persona principal do nosso público-alvo. Isso serve como a fundação estratégica para todo o projeto.

---
## 1.1. Problema Endereçado

A loja online de produtos artesanais e personalizados enfrenta dois desafios cruciais:

* **Alta Taxa de Abandono de Carrinho:** Um percentual significativo de visitantes adiciona itens ao carrinho, mas não finaliza a compra. Isso representa uma perda direta de receita e um alto custo de aquisição de clientes sem o devido retorno.
* **Baixa Taxa de Recompra:** Clientes que compram pela primeira vez raramente retornam para uma segunda compra. A falta de um processo estruturado de engajamento pós-venda resulta em oportunidades perdidas de fidelização e Lifetime Value (LTV) reduzido.

Estas questões resultam em vendas perdidas, ROI negativo em campanhas de marketing e um crescimento estagnado da base de clientes fiéis.

---
## 1.2. Objetivos da Automação (KPIs)

O principal objetivo deste projeto é otimizar o funil de vendas e o relacionamento com o cliente através da automação. Os Key Performance Indicators (KPIs) para medir o sucesso são:

* **Objetivo Principal:**
    * Aumentar a **taxa de recuperação de carrinho abandonado** em **15%** nos próximos 3 meses.
    * (Métrica: % de carrinhos abandonados que são convertidos em vendas.)

* **Objetivos Secundários:**
    * Aumentar a **taxa de recompra** (clientes que realizam uma segunda compra) em **10%** no mesmo período.
    * (Métrica: % de clientes que fazem uma segunda compra após X dias da primeira.)
    * Melhorar a **experiência do cliente no pós-compra**, gerando mais satisfação e potenciais avaliações positivas.
    * (Métrica: Taxa de abertura e cliques dos e-mails de pós-compra, número de avaliações geradas.)

---
## 1.3. Persona Principal

Para direcionar nossas automações de forma eficaz, focamos em uma persona que representa nosso cliente ideal:

### Clara, a Designer Criativa

* **Dados Demográficos:**
    * Idade: 28 anos
    * Ocupação: Designer Freelancer
    * Localização: Centro urbano, apartamento pequeno, valoriza itens decorativos e presentes únicos.

* **Desafios:**
    * Dificuldade em encontrar produtos que sejam verdadeiramente originais e não massificados.
    * Frequentemente adiciona itens ao carrinho online para "pensar" ou comparar, mas acaba se distraindo e esquecendo.
    * Prefere compras online por conveniência, mas valoriza uma experiência de compra personalizada.

* **Objetivos:**
    * Descobrir presentes criativos e itens de decoração artesanais que reflitam sua personalidade e estilo de vida.
    * Encontrar lojas online confiáveis que ofereçam produtos de alta qualidade e um bom atendimento.

* **Comportamento Online:**
    * Ativa no Instagram e Pinterest, seguindo perfis de design de interiores e artesãos.
    * Pesquisa por "presentes únicos", "decoração artesanal" em motores de busca.
    * Sensível a ofertas e descontos, mas mais motivada pela exclusividade do produto.
    * Recebe muitas newsletters, mas só abre as que realmente chamam atenção.

---
## 1.4. Mapeamento da Jornada do Cliente e Pontos de Contato

A jornada da Clara em relação à nossa loja online é mapeada com foco nos pontos onde a automação será aplicada:

### Jornada do Cliente
* **Consciência:** Clara sente a necessidade de encontrar um presente único ou um item de decoração que combine com seu estilo.
* **Consideração:** Ela pesquisa online, encontra nossa loja através de redes sociais ou busca orgânica, e navega pelos produtos.
* **Decisão (Abandono de Carrinho):** Clara adiciona alguns produtos ao carrinho, mas hesita em finalizar a compra (talvez por distração, querer comparar ou pensar mais sobre o valor). **Este é um ponto crucial para a automação de recuperação.**
* **Compra:** Clara finaliza a compra com sucesso.
* **Pós-Compra/Retenção:** Após receber o produto, há uma oportunidade de solicitar feedback e incentivar futuras compras. **Este é outro ponto crucial para a automação de pós-venda.**
* **Fidelização:** Cliente satisfeito retorna e se torna um comprador recorrente.

### Pontos de Contato Chave para Automação
* **Carrinho de Compras Online:** Principal gatilho para o fluxo de recuperação de carrinho.
* **E-mail:** Canal primário para envio de lembretes, nutrição, confirmações e recomendações.
* **Plataforma de E-commerce (Shopify):** Fonte dos dados de carrinho abandonado e de compra finalizada.
* **Plataforma de Automação de Marketing (Klaviyo):** Onde os fluxos serão criados e gerenciados.
* **WhatsApp/SMS (Conceitual):** Potencial canal para lembretes rápidos e confirmações (via módulo Python).