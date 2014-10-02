def fakultet(nmr):
    fakultet = nmr
    if nmr == 0:
        return 1
    else:
        while nmr > 1:
            nmr = nmr - 1
            fakultet = fakultet * nmr
        return fakultet

fakultet(5)



