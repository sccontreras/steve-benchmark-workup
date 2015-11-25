__author__ = 'stevebertolani'

from re import search,compile

# Below is a parser for the command line output from various hmmer and esl tools

# One for the esl-alipid

#class Alipid(object):
#    def __init__(self):
#        self.dict = dict()


    #should I make this use a pandas dataframe?

class AlipidLine(object):

    def __init__(self,line):
        line = line.rstrip('\n')
        myline = line.split()
        #assert len(line) == 5
        self.target = myline[0]
        self.name = myline[1]
        self.pid = float(myline[2])
        self.beginpos = int(myline[3])
        self.endpos = int(myline[4])
        self.pdb = False
        self.check_name()

    def check_name(self):
        mysplit = self.name.split('_')
        myreg = compile('[A-Z]')
        if len(mysplit) == 2:
            if len(mysplit[0]) ==4:
                if myreg.search( mysplit[1] ):
                    #print "This is probably a PDB code"
                    self.pdb = True
