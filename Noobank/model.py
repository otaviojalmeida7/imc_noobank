"""
===============================================================================
MODEL — camada de DADOS e REGRAS DE NEGÓCIO (padrão MVC)
===============================================================================
Este é o ÚNICO arquivo de Model do projeto. Ele reúne:

    1) As classes que representam os DADOS do app (Transaction e Contact);
    2) A classe principal do Model — `BankAccount` — que guarda o estado da
       conta (saldo, extrato, contatos) e concentra TODAS as regras de
       negócio (ex.: "não pode transferir valor <= 0", "saldo não pode
       ficar negativo"). Nem a View nem o Controller sabem esses detalhes;
       eles só chamam os métodos que o Model oferece.

O Model NUNCA importa `flet` e NUNCA sabe desenhar nada na tela. Ele só
guarda e manipula dados. Quem desenha é a View; quem decide "quando" chamar
o quê é o Controller.

"""

# ABC e abstractmethod são as ferramentas do Python para criar classes e
# métodos abstratos (paradigma de ABSTRAÇÃO).
from abc import ABC, abstractmethod

# dataclass evita ter que escrever o __init__ "na mão" para classes que só
# guardam dados
from dataclasses import dataclass

# Usado só pra pegar a data atual (dia/mês) de uma nova transação de Pix
from datetime import datetime


