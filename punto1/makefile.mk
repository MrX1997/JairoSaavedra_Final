all:
	gcc OPENMP.c -o sample.x  -fopenmp -lm
	./sample.x
	python plots.py
	
