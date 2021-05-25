import os

class H1D(object):

    def __init__(self):
        self.EXE = 'H1D_CALC.EXE'

    def exec(self, project):
        print ('\n\n\n RUNS PROJECT {} \n\n\n'.format(project))
        cmd = "./{} {}".format(self.EXE, project)
        os.system(cmd)
