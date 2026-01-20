#!/usr/bin/python3
def multiple_returns(sentence):
    retlist = list(sentence)
    if retlist == []:
        return (0, None)
    else:
        return len(retlist), retlist[0]
