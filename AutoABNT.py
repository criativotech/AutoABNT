import uno

def AplicarFormatacaoABNT(*args):
    try:
        doc = XSCRIPTCONTEXT.getDocument()
        
        # Margens ABNT
        estilos_pagina = doc.getStyleFamilies().getByName("PageStyles")
        estilo_padrao_pag = estilos_pagina.getByName("Standard")
        estilo_padrao_pag.TopMargin = 3000
        estilo_padrao_pag.LeftMargin = 3000
        estilo_padrao_pag.RightMargin = 2000
        estilo_padrao_pag.BottomMargin = 2000
        
        # Corpo do Texto
        estilos_para = doc.getStyleFamilies().getByName("ParagraphStyles")
        corpo = estilos_para.getByName("Standard")
        corpo.CharFontName = "Arial"
        corpo.CharHeight = 12
        corpo.ParaAdjust = 2  # Justificado
        
        # Espaçamento 1,5
        ls = uno.createUnoStruct("com.sun.star.style.LineSpacing")
        ls.Height = 150
        corpo.ParaLineSpacing = ls
        
        # Recuo 1,25cm
        corpo.ParaFirstLineIndent = 1250 
        
    except Exception as e:
        # Isso ajuda a diagnosticar erros em máquinas de amigos
        print(f"Erro: {str(e)}")
    
    return None
