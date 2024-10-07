cdef extern from "stdio.h":
    void printf(const char *format, ...)

cdef extern void execute():
    printf("PyCon APAC 2024 (cython)\n")
