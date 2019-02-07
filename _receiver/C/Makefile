# Makefile for compiling Hydra DSP code
# Version : 1.0
# Date: August 2018
# Author: Tamás Pető
CC=gcc
CFLAGS=-Wall -march=native -O3
RM= rm -f

all: rtl_daq sync gate sim

rtl_daq: rtl_daq.c rtl_rec.h
	$(CC) $(CFLAGS) rtl_daq.c -lpthread -lrtlsdr -o rtl_daq

sync: sync.c sync.h
	$(CC) $(CFLAGS) sync.c -lpthread -o sync
gate: gate.c
	$(CC) $(CFLAGS) gate.c -lpthread -o gate
sim: sim.c
	$(CC) $(CFLAGS) sim.c -o sim
clean:
	$(RM) rtl_daq sync gate sim
