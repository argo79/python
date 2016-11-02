def secondi(hh, mm, ss):
	nsec=hh*3600
	nsec=nsec+(mm*60)
	nsec=nsec+ss
	return nsec

print secondi(2,1,11)
