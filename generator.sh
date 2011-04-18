#!/bin/bash
export PYTHONPATH=/usr/lib/libreoffice/basis3.3/program
export LD_LIBRARY_PATH=/usr/lib/libreoffice/basis3.3/program

soffice "-accept=socket,host=localhost,port=2002;urp;" &> /dev/null
./generator.py "$@"
killall soffice.bin
