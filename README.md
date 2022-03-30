# Out loud thoughts
Out loud thoughts about everything.

## Requirements
Python 3.10.0

## Utils

#### utils/timeit.py
Simple wrapper for time measure

### Compare _native_ and _pydantic_ dataclasses

All measurements done in loop of 1 000 000

Measuring results in table presented in seconds.

| Action          | Native        | Pydantic     |
| --------------- | ------------- | ------------ |
| create          | ~0.444041479  | ~5.404597358 |
| convert to dict | ~5.510993991  | ~5.175302796 |
| get attribute   | ~0.054861316  | ~0.049166930 |
| set attribute   | ~0.064916138  | ~0.538404490 |
