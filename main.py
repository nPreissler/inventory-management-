# 1 - Adição de produtos
# -- 1.1 - Adição de mais de um produto 
# -- 1.2 - ID generativo
# -- 1.3 - Quantidade do produto
# 2 - Pesquisa de produto
# -- 2.1 - Pesquisa por ID
# -- 2.2 - Pesquisa Filtrada por letras que as palavras contém
# 3 - Remoção de produtos
# -- 3.1 - Remoção de mais de um produto
# -- 3.2 - Remoção por ID
# 4 - Desligamento do programa 

# -- Todas as operações devem ter como ser canceladas a qualquer momento

from models.product import Product
import os
import time

stock = []
