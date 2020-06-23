class PostScriptDoc:
    '''
    Purpose:
    A class for representing a document in PostScript format.

    Description:
    Using this class one can interactively create PostScript 
    documents from Python programs.
    
    You first initialize a document,
    fig = PostScriptDoc()
    and add PostScript command lines, comments function definitions, text, 
    fig.add('newpath')
    fig.add('20 100 moveto')
    fig.add('200 150 lineto')
    fig.add('stroke')
    fig.addText('Helvetica',12, 50, 100, 'Hello World!')
    and finally you can save the document for printing.
    fig.save() 

    Data members are:
    name - a string with the document name.
    pformat - a string denoting paper format, like 'a4'.
    data - a list of strings, where each list element list is 
    a line in the final PostScript document.

    Author:
    Nikola Mirkov (nikolamirkov@yahoo.com)

    '''
    def __init__(self,name,pformat):
        self.name = name + '.ps'
        self.paper_format = pformat
        self.data = ['%!Adobe-PostScript-3.0']

    def add(self, line):
        self.data.append(line)

    def addComment(self,comment):
        '''Arguments :
           comment - a string
        '''
        line = "%%" + comment 
        self.data.append(line)

    def addText(self, fontType, fontSize, xpos, ypos, text):
        '''Arguments:
           fontType - a string, eg. 'Times-Roman', 'Helvetica'
           fontSize - an integer, e.g. 10, 12, 14, etc.
           xpos,ypos - integers
           text - text to appear in PostScript document
        '''
        self.data.append( '/'+ str(fontType) + ' findfont ' + str(fontSize) +' scalefont setfont' )
        self.data.append( str(xpos) + ' ' + str(ypos) + ' moveto ('+ text +') show')

    def addDef(self, def_name, func_body):
        '''Adds function definition to a document.
           Arguments:
           def_name - a string, a name of the function
        '''
        self.data.append('/'+ str(def_name) + ' { ' + str(func_body) + ' } def' )

    def save(self):
        # final command in the document
        self.data.append('showpage')
        with open(self.name, 'w') as f:
            f.writelines("%s\n" % l for l in self.data)
        f.close()


class BuffonFig(PostScriptDoc):
    '''A Post Script document made specifically to plot results of Buffon needle experiment.'''

    def __init__(self,name,num_needles):
        PostScriptDoc.__init__(self, name, 'a4')
        self.num_needles = num_needles

        self.addComment('Reconstruction of Fig. 1.10 from' + 
            'Werner Krauth - Statistical Mechanics - Algorithms and Computation.')
        self.addDef( 'l', 
                     '25 0 translate ' +
                     'newpath ' +
                     '0 100 moveto ' +
                     '0 800 lineto ' +
                     'stroke')
        self.addDef( 'ndlnohit',
                     'newpath ' +
                     '0 0 moveto ' +
                     '25 0 lineto ' +
                     'stroke ' +
                     'newpath ' +
                     '2 0 2 0 360 arc closepath ' +
                     'stroke ')
        self.addDef( 'ndlhit',
                     'newpath ' +
                     '0 0 moveto ' +
                     '25 0 lineto ' +
                     'stroke ' +
                     'newpath ' +
                     '12.5 0 1 0 360 arc closepath ' +
                     'fill ' +
                     'stroke ' +
                     'newpath ' +
                     '2 0 2 0 360 arc closepath ' +
                     'stroke')
        self.addText('Times-Roman',12,150,50,"Fig. 1.10 Buffon's experiment with "+
                      str(self.num_needles) + 
                      " needles (a=b).")
        self.add('0.1 setlinewidth 1 setlinecap 0 setgray')
        self.add('50 0 translate')
        self.add('l l l l l l l l l l l l l l l l l l l l')
        self.add('-475 100 translate')
        self.add('0.2 setlinewidth')

    def addNeedle(self,xpos,ypos,angle,hit):
        '''Places a needle on a plot, given the x,y position of the tail, 
        angle of rotation, and a boolean which determines 
        is needle crossing the grid line or not.'''
        self.add(str(xpos) +' '+ str(ypos) +' translate')
        self.add( str(angle) +' rotate')
        if(hit):
            self.add('1 0 1 setrgbcolor')
            self.add('ndlhit')
        else:
            self.add('0 1 0 setrgbcolor')
            self.add('ndlnohit')
        self.add('360 ' + str(angle) + ' sub rotate')
        self.add(str(-1*xpos) +' '+ str(-1*ypos) +' translate')
