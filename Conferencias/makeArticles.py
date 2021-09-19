import os





names = []
fullnames = []
for i in open('texto.txt').readlines():
    p = i[0:-1]
    fullnames.append(p)
    s = i.replace(' ', '_')
    if len(s) > 65:
        s = s[0:65]
    else:
        s = s[0:-1]
    s = s + '.pdf'
    names.append(s)


for i in range(1, 14):

    directory = './Conferencia_' + str(i)
    directoryGood = './ConferenciaGood_' + str(i) + '/Investigacion_Conferencias_' 
    #dirs = os.listdir(directory)
    #target = directory + '/' + dirs[0]
    #command = 'cp ' + target + ' ' + directoryGood + names[i-1]
    #print command
    print '\\subsubsection{' + fullnames[i-1] + '}'
    print '\\includepdf[pages=-]{Conferencias/Investigacion_Congresos_' + names[i-1] + '}' 




