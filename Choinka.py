iloscGalezi = 10
for nrGalezi in range(iloscGalezi):
    galaz = " "*(iloscGalezi-nrGalezi)+"#"*(nrGalezi*2+1)
    print(galaz)
    if(nrGalezi>2):
        print(" "*(iloscGalezi-1)+"|||")
    else:
        print(" "*(iloscGalezi-1)+" | ")
