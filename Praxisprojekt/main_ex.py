from pipeline_ex import ETL
from analysis_ex import Analyser

figure_save_path = "C:/res/pythonDHBW"
pipeline = ETL("data_specs.json")
final_table, engine_table = pipeline.run()
analyser = Analyser(final_table, engine_table, figure_save_path=figure_save_path)
analyser.run()
