#def do_t(string):
#    answer = float(string[(string.find(':'))+1:].lstrip())
#    return answer
text = "X-DSPAM-Confidence:    0.8475"
#print do_t(text)

###short example
print float(text[(text.find(':'))+1:].lstrip())
