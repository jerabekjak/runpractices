import os
import shutil

class H1D(object):

    def __init__(self, benchmark, line):
        self.EXE = 'H1D_CALC.EXE'
        self.__bm_path = benchmark
        self.__line = int(line)

    def exec(self, project):
        print ('\n\n\n RUNS PROJECT {} \n\n\n'.format(project))
        cmd = "./{} {}".format(self.EXE, project)
        os.system(cmd)

    def prepare_project(self, project_dir, scenario, ipar, jpar):
        """ project dir :: where the config and output files 
        fill be stored
        scenario :: is on row in the from the scenario csv
        ipar :: which parameter in scenario list is to be scaled
        return T/F :: if parameter is not scalabel false
        """


        i = ipar -5
        j = jpar -5

        scale = scenario[5:10]
        # scale = [float(j) for j in scale]
        if 'NA' in scale[i] : return False
        if 'NA' in scale[j] : return False
        scale[i] = float(scale[i])
        scale[j] = float(scale[j])

        # duplicate benchmarkproject
        self.duplicate_project(self.__bm_path, project_dir)

        # read  benchmark parameters
        selector = os.path.join(project_dir, 'SELECTOR.IN')
        with open(selector, 'r') as f_:
            for k, line in enumerate(f_):
                if k == self.__line-1 : 
                    params_orig = line.split()

        params_orig = [float(k) for k in params_orig]
        params_new = params_orig.copy()
        # for  i in range(len(scale)) :
        params_new[i] = params_orig[i] * scale[i]
        params_new[j] = params_orig[j] * scale[j]

        s = [str(i) for i in params_new]
        res = "  ".join(s) + '\n'

        # replace line
        with open(selector, 'r') as f_:
            lines = f_.readlines()
        lines[self.__line-1] = res
        with open(selector, 'w') as f_:
            f_.writelines(lines)

        return True
            

    def duplicate_project(self, src, dst):

        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)

            shutil.copy2(s, d)
        


