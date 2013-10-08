
def isDnaRnaOrProtein(aString):
    """Attempts to determinine the data type by the composition.

    Returns 1 for DNA, 2 for RNA, and 0 for protein.  Or so it thinks.

    It only works for lowercase symbol letters.
    """
    nGaps = string.count(aString, '-')
    nQs = string.count(aString, '?')
    strLenNoGaps = len(aString) - (nGaps + nQs)
    acgn = (string.count(aString, 'a') +
           string.count(aString, 'c') +
           string.count(aString, 'g') +
           string.count(aString, 'n'))
    t = string.count(aString, 't')
    u = string.count(aString, 'u')
    if 0:
        print("stringLength(no gaps) = %s" % strLenNoGaps)
        print("acgn = %f" % acgn)
        print("t = %f" % t)
        print("u = %f" % u)

    # If it is 90% or better acgn +t or +u, then assume it is dna or rna
    threshold = 0.9 * strLenNoGaps
    if acgn + t >= threshold:
        return 1
    elif acgn + u >= threshold:
        return 2

    # At this point we still don't know.  It might be dna or rna with
    # lots of ambigs.  But we will only allow that if the content of
    # acgn +t or +u is more than threshold1.  That should
    # prevent eg 'rymkswhvd' from being assigned as dna.
    
    threshold1 = 0.75 * strLenNoGaps
    tally = (string.count(aString, 'r') +
             string.count(aString, 'y') +
             string.count(aString, 'm') +
             string.count(aString, 'k') +
             string.count(aString, 's') +
             string.count(aString, 'w') +
             string.count(aString, 'h') +
             string.count(aString, 'b') +
             string.count(aString, 'v') +
             string.count(aString, 'd') )
    threshold2 = 0.99 * strLenNoGaps
    #print "  string length is %i, strLenNoGaps is %i" % (len(aString), strLenNoGaps)
    #print "  threshold2 is %3.1f, acgn + t + ambigs = %i" % (threshold, (acgn + t + tally))
    #print "  threshold1 is %3.1f, acgn + t = %i" % (threshold, (acgn + t))
    if (acgn + t + tally >= threshold2) and (acgn + t >= threshold1):
        return 1
    elif (acgn + u + tally >= threshold2) and (acgn + u >= threshold1):
        return 2
    else:
        return 0
