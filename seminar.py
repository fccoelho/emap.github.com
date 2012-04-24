#!/usr/bin/env python
#-*- coding: utf-8 -*-
u"""
Script para gerar página de seminário para o site da EMAp

Exemplo de uso:
./seminar.py -a "ze mané" -t "o título da palestra" -r resumo.txt -b "bla bla bla" -d 2012 4 20
[2012, 4, 20, 'o titulo da palestra']
"""

#import requests
import argparse
import codecs
#import datetime


template = u"""
---
layout: seminar
title: %(titulo)s
quem: %(autor)s
onde: FGV -- Praia de Botafogo, 190, sala 317
---

- Quem:  {{ page.quem }}
- Onde:  {{ page.onde }}
- Quando: {{ page.date | date_to_string }} às 16:00

%(resumo)s

## Info sobre palestrante

%(bio)s

## Observação para visitantes

A presença é gratuita e não exige confirmação. A FGV não permite a
entrada de homens vestindo bermuda ou chinelo.

"""

import sys


def gera_pagina(args):
    u"""
    Gera a página em formato markdown com base no template.
    """
    with codecs.open(args.resumo, 'r', encoding=sys.getfilesystemencoding()) as f:
        res = f.read()
    d = {'titulo':args.titulo.decode('utf-8'),
        'autor': args.autor.decode('utf-8'),
        'resumo': res,
        'bio': args.bio.decode('utf-8'),
        }
    
    t = args.data
    t.append(args.titulo)
    pname = "%s-%s-%s-%s.md"%tuple(t)
    with codecs.open(pname,'w', encoding="utf-8") as f:
        texto = template % d
        f.write(texto)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Gera um pagina de seminário no formato requerito para a EMAP')
    parser.add_argument('-a', '--autor', required=True,help='Nome do palestrante')
    parser.add_argument('-t', '--titulo', required=True, help="titulo do seminario")
    parser.add_argument('-r', '--resumo',required=True, help="nome do arquivo contendo o abstract")
    parser.add_argument('-b','--bio',help="Pequena biografia do autor")
    parser.add_argument( '-d', '--data', metavar='D', type=int, nargs=3, required=True, help="Data do seminario: <ano mes dia> ")

    args = parser.parse_args()

    gera_pagina(args)
