project x:
  local_dir = ~/abc
  remote_dir = /afs/abc
  
  project a:
    A = common.c
    B = main.c
    C = common.o [gcc -o common.o common.c -c]
    D = main.o [gcc -o main.o main.c -c]
    E = c [gcc -o c main.o common.o]
  
    C -> A
    D -> B
    E -> C
    E -> D