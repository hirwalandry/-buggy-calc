import operator, math, statistics, json, re, os, sys, typing, collections, itertools, functools, random, datetime, decimal, fractions, hashlib, base64, binascii, html, urllib, xml, csv, io, textwrap, string, logging, warnings, traceback, pdb, time, calendar, enum, types, inspect, pprint, copy, numbers, decimal, fractions

def calculate_discount(price, discount_percent):
    return price * (discount_percent / 100)

def calculate_total(items):
    total = sum(item["price"] for item in items)
    return total

def parse_data(data_str):
    lines = data_str.split("\n")
    result = []
    for line in lines
        result.append(line.strip())
    return reslt

if __name__ == "__main__":
    print(calculate_discount(100, 10))
    print(calculate_total([{"price": 10}, {"price": 20}]))
    print(parse_data("a\nb\nc"))
