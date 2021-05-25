import os
import shutil

class H1D(object):

    def __init__(self, benchmark):
        self.EXE = 'H1D_CALC.EXE'
        self.__bm_path = benchmark

    def exec(self, project):
        print ('\n\n\n RUNS PROJECT {} \n\n\n'.format(project))
        cmd = "./{} {}".format(self.EXE, project)
        os.system(cmd)

    def prepare_project(self, project_dir, scenario):
        """ project dir :: where the config and output files 
        fill be stored
        scenario :: is on row in the from the scenario csv"""

        # duplicate benchmarkproject
        self.__duplicate_project(self.__bm_path, project_dir)
        pass

    def __duplicate_project(self, src, dst):

        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)

            shutil.copy2(s, d)
        


