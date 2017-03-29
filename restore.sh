#read qr codes into file pieces using zbarimg

#zbarimg -q code.png > out.part 
#zbarimg -q	quiet
#	--raw	only output data

#ISSUES: zbar img appends a newline to the end of output
#i guess just strip?

#cat file pieces back in to one file
#cat xa{a..g} -> xaa, xab, xac, xad....xag 

#untar tarball -> origional directory 
