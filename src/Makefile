CC = g++
CFLAGES = -g
CPPFLAGES = -Wall -pedantic

EXE = main

.PHONY: clean all 

all: $(EXE)

main: main.cpp OneLineSolver.o

OneLineSolver.o: OneLineSolver.cpp OneLineSolver.hpp

clean:
	$(RM) *.o $(EXE)
