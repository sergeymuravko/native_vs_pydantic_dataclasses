# Out loud thoughts
Out loud thoughts about everything.

## Requirements
Python 3.10.0

## Utils

#### utils/timeit.py
Simple wrapper for time measure

##### Compare native and pydantic dataclasses

All measurements done in loop of 1 000 000
Measuring results in table presented in seconds

| Action           | Native        | pydantic     |
| ---------------- | ------------- | ------------ |
| create           | ~0.444041479  | ~5.404597358 |
| convert to dict  | ~5.510993991  | ~5.175302796 |
