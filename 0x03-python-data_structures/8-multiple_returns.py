#!/usr/bin/python3


def multiple_returns(sentence):
    first = 0
    return (
        len(sentence),
        sentence[first] if sentence[first] else None
    )
