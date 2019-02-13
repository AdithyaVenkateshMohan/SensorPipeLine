#!/usr/bin/python2

import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    execmode =''
    try:
        opts, args = getopt.getopt(argv,"hi:o:e:",["ifile=","ofile=", "ExecMode="])
   
    except getopt.GetoptError:
        print 'test.py -f <inputfile> -o <outputfile> -e <execmode>'
        sys.exit(2)
    
    for opt, arg in opts:
        if opt == '-h':
            print 'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-e", "--execmode"):
            execmode = arg
    
            
    print 'Input file is "', inputfile
    print 'Output file is "', outputfile
    print "the input exec mode is", execmode

if __name__ == "__main__":
    main(sys.argv[1:])
