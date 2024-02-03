import sys

#print("Executable 'sys.executable' = " + str(sys.executable))


# PYTHONHOME = sys.prefix
#print("PYTHONHOME 'sys.prefix' = " + str(sys.prefix))

# PYTHONPATH = sys.path
#print("PYTHONPATH 'sys.path' = " + str(sys.path))
for path in sys.path: print("PYTHONPATH 'sys.path' = " + str(path))

# PYTHONPLATLIBDIR = sys.platlibdir
#print("PYTHONPLATLIBDIR 'sys.platlibdir' = " + str(sys.platlibdir))