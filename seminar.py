#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""
Script para gerar página de seminário para o site da EMAp
"""

import requests
import argparse
import datetime


template = """
---
layout: seminar
title: %(titulo)
quem: %(autor)
onde: FGV -- Praia de Botafogo, 190, sala 317
---

- Quem:  {{ page.quem }}
- Onde:  {{ page.onde }}
- Quando: {{ page.date | date_to_string }} Ã s 16:00

%(resumo)

## Info sobre palestrante

%(bio)

## ObservaÃ§Ã£o para visitantes

A presenÃ§a Ã© gratuÃ­ta e nÃ£o exige confirmaÃ§Ã£o. A FGV nÃ£o permite a
entrada de homens vestindo bermuda ou chinelo.

"""

def gera_pagina(args):
	"""
	Gera a página em formato makdown com base no template.
	"""
	d = {'titulo':args.t,
		'autor': args.a,
		'resumo': args.r,
		'bio': args.b
		}
	pname = "%s-%s-%s-%s.md"%tuple(args.data.append(args.t))
	with open(pname,'w') as f:
		f.write(template%d)
	
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Gera um pagina de seminário no formato requerito para a EMAP')
	parser.add_argument('-a', '--autor', required=True,help='Nome do palestrante')
	parser.add_argument('-t', '--titulo', required=True, help="titulo do seminario")
	parser.add_argument('-r', '--resumo',required=True, help="nome do arquivo contendo o abstract")
	parser.add_argument('-b','--bio',help="Pequena biografia do autor")
	parser.add_argument( '-d', '--data', metavar='D', type=int, nargs=3, required=True, help="Data do seminario: <dia mes ano> ")

	args = parser.parse_args()
