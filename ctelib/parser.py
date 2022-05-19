import sys
from lxml import etree as etree_
from . import ctelib as supermod

def parsexml_(infile, parser=None, keep_signature=False, **kwargs):
    if parser is None:
        parser = etree_.ETCompatXMLParser()
    
    doc = etree_.parse(infile, parser=parser, **kwargs)
    if doc.getroot().tag == "{http://www.portalfiscal.inf.br/cte}cteProc":
        root = doc.getroot()[0]
    else:
        root = doc.getroot()

    if not keep_signature:
        for child in root:
            if child.tag in ["{http://www.w3.org/2000/09/xmldsig#}Signature",
                             "{http://www.w3.org/2000/09/xmldsig#}\
                             ds:Signature"]:
                root.remove(child)
    subtree = etree_.ElementTree(root)
    return subtree

def export(doc, cteProc=True, stream=sys.stdout):
    stream.write('<?xml version="1.0" ?>\n')
    if cteProc:
        stream.write('<cteProc xmlns="http://www.portalfiscal.inf.br/cte" \
                         versao="4.00">\n')
    doc.export(stream, 0, namespaceprefix_='', name_='CTe',
               namespacedef_='xmlns="http://www.portalfiscal.inf.br/cte"')
    if cteProc:
        # TODO deal with infProt
        stream.write('</cteProc>\n')

def parse(inFile, silence=False):
    doc = parsexml_(inFile)
    rootNode = doc.getroot()
    rootTag, rootClass = supermod.get_root_tag(rootNode)
    if rootClass is None:
        rootClass = supermod.TCTe
    rootObj = rootClass.factory()
    rootObj.build(rootNode)

    doc = None
    if not silence:
        export(rootObj)
    
    return rootObj

