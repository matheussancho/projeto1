CC = gcc
CFLAGS = -Wall -std=c99
LIBS = -lm

SRC = prog.c soma.c media.c maior.c
OBJ = $(SRC:.c=.o)
EXECUTABLE = programa

all: $(EXECUTABLE)

$(EXECUTABLE): $(OBJ)
	$(CC) $(CFLAGS) -o $@ $(OBJ) $(LIBS)

%.o: %.c
	$(CC) $(CFLAGS) -c $<

clean:
	rm -f $(OBJ) $(EXECUTABLE)
