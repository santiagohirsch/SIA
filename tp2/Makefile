create_config:
	cp config_options.json config.json

run:
	pipenv run python main.py config.json > output/output.txt

crossing:
	rm -rf output/crossing_method.csv
	pipenv run python crossing_method_generator.py

mutation:
	rm -rf output/mutation_method.csv
	pipenv run python mutation_method_generator.py

selection:
	rm -rf output/selection_method.csv
	pipenv run python selection_method_generator.py

replacement:
	rm -rf output/replacement_method.csv
	pipenv run python replacement_method_generator.py

crossing_analysis:
	pipenv run python output/crossing_analysis.py

mutation_analysis:
	pipenv run python output/mutation_analysis.py

selection_analysis:
	pipenv run python output/selection_analysis.py

replacement_analysis:
	pipenv run python output/replacement_analysis.py

crossing_graphs:
	pipenv run python output/crossing_graphs.py

mutation_graphs:
	pipenv run python output/mutation_graphs.py