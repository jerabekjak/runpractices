class Practices:
    def __init__(self, parser):
        self.__tsc_path = parser.table_scenarios
        self.__bm_path = parser.benchmark_model
        self.__line = parser.line
        self.__out_dir = parser.output_dir

        # tables columns meaning
        self.__c_zero_scenario = 4
        self.__c_params = range(5,9)


    def run(self):
        table = self.__read_csv()

        for i in range(1,len(table)):
            zc = table[i][self.__c_zero_scenario]
            if not(zc == 'NA'):
                if int(zc) != 1 :
                    self.__run_scenario(table[i])

    def __run_scenario(self, tabline):
        print (tabline)
        for i in self.__c_params:
            print (i)

#    def __scenaricore(self, tabline):
#        return(

    def __read_csv(self):
        with open(self.__tsc_path, 'r') as file_:
            lines = file_.readlines()
        
        csv = []
        for line in lines:
            csv.append(line.replace('\n', '').split(','))
        
        return(csv)

