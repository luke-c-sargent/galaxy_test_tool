#!/usr/bin/env python

import sys

class SequenceDigest(object):
    def incA(self):
        self.A+=1
    def incT(self):
        self.T+=1
    def incG(self):
        self.G+=1
    def incC(self):
        self.C+=1
    def incU(self):
        self.U+=1
    def incN(self):
        self.N+=1


    incrementer = {}

    incrementer["A"] = lambda s: s.incA()
    incrementer["T"] = lambda s: s.incT()
    incrementer["G"] = lambda s: s.incG()
    incrementer["C"] = lambda s: s.incC()
    incrementer["U"] = lambda s: s.incU()
    incrementer["N"] = lambda s: s.incN()
    incrementer['\n'] = lambda s: s



    def __init__(self, sequence_id):
        self.seqID = sequence_id
        self.A = 0
        self.T = 0
        self.G = 0
        self.C = 0
        self.U = 0
        self.N = 0


    def parseLine(self, line):
        for char in line:
            self.incrementer[char](self)

    def percent_stringer(self, val,total):
        return str(val) + '\t[{:2.4f}'.format(100.0*(float(val)/total)) + '%]\n'

    def stringify(self):
        result = self.seqID
        total = self.A + self.T + self.G + self.C + self.U
        result += "Total Base Pairs:" + str(total) + '\n'
        result += "Total Adenosine :" + self.percent_stringer(self.A,total)
        result += "Total Thymidine :" + self.percent_stringer(self.T,total)
        result += "Total Guanine   :" + self.percent_stringer(self.G,total)
        result += "Total Cytidine  :" + self.percent_stringer(self.C,total)
        result += "Total Uridine   :" + self.percent_stringer(self.U,total)
        result += "Total Any       :" + self.percent_stringer(self.N,total) + '\n'

        result += "AT Ratio        :" + self.percent_stringer(self.A+self.T, total)
        result += "GC Ratio        :" + self.percent_stringer(self.G+self.C, total) + '\n\n'

        return result



def __main__():
    args = sys.argv
    print str(args)
    output = open( args[2], 'wb' )
    final_result = ""
    digest = SequenceDigest("init")
    with open( args[1], 'rb' ) as input:
        for line in input:
            print line
            if line[0] is '>':
                digest.__init__(line)
            elif line[0] == '\n':
                final_result += digest.stringify()
            else:
                digest.parseLine(line)
    print final_result
    output.write(final_result)
    output.close()



if __name__=="__main__": __main__()