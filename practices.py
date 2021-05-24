class Practices:
    def __init__(self, parser):
        self.__tsc_path = parser.table_scenarios
        self.__bm_path = parser.benchmark_model
        self.__line = parser.line
        self.__out_dir = parser.output_dir


    def run(self):
        table = self.read_csv()

        for i in range(1,len(table)):
            (table[i][4]
            




    def read_csv(self):
        with open(self.__tsc_path, 'r') as file_:
            lines = file_.readlines()
        
        csv = []
        for line in lines:
            csv.append(line.replace('\n', '').split(','))
        
        return(csv)

