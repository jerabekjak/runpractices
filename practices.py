import os
import shutil

import h1d

class Practices:
    def __init__(self, parser):
        self.__tsc_path = parser.table_scenarios
        self.__bm_path = parser.benchmark_model
        self.__line = parser.line
        self.__out_dir = parser.output_dir

        # tables columns meaning
        self.__c_zero_scenario = 4
        self.__c_params = range(5,10)
        self.__pars_name = ['','','','','','Qr','Qs','a','n','Ks']

        self.__h1d = h1d.H1D()


    def run(self):

        # read table with scenarios
        table = self.__read_csv()
        self.__h1d.exec(self.__bm_path)

        # compute scenarios
        for i in range(1,len(table)):
            zc = table[i][self.__c_zero_scenario]
            if not(zc == 'NA'):
                if int(zc) != 1 :
                    self.__run_scenario(table[i])

    def __run_scenario(self, tabline):
        for i in self.__c_params:
            scenariocode = self.__scenariocode(self.__pars_name[i], tabline)
            outdir = self.__make_outdir(scenariocode)

    def __make_outdir(self, scenarioname):
        outdir = os.path.join(self.__out_dir, scenarioname)
        if os.path.exists(outdir):
            shutil.rmtree(outdir)
        os.mkdir(outdir)
        return outdir

    def __scenariocode(self, parname, tl):
        return("{}-{}-{}-{}-{}-{}".format(tl[0].strip().zfill(2),
        tl[1].strip(),tl[2].strip(),tl[3].strip(),tl[4].strip(),parname))

    def __read_csv(self):
        with open(self.__tsc_path, 'r') as file_:
            lines = file_.readlines()
        
        csv = []
        for line in lines:
            csv.append(line.replace('\n', '').split(','))
        
        return(csv)

