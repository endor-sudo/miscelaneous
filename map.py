#! /usr/bin/env python3
"""Pesquisa por um local no Google Maps"""
import webbrowser, sys

address="http://www.google.com/maps/search/"+" ".join(sys.argv[1:])
webbrowser.open(address)
