# SmarterTechnologies-BoxSorter
Coding challenge for Smarter Technologies

## Instructions

- **Run the sorter (manual invocation):**

	Use Python to import and call the `sort` function from `sort.py`.

	Example from an interactive prompt or a script:

	```python
	from sort import sort

	status = sort(10, 20, 30, 5)
	print(status)  # STANDARD
	```

- **Run the unit tests:**

	From the project root run:

	```bash
	python -m unittest tests.test_sort -q
	```

	Or let unittest discover all tests with:

	```bash
	python -m unittest -q
	```
