
import nltk

# Ingles
gramatica_ingles = r"""
  NP: {<DT|PP\$>?<JJ>*<NN>} 
      {<NNP>+}                
"""
cp_ingles = nltk.RegexpParser(gramatica_ingles)


oracion = [("the", "DT"), ("little", "JJ"), ("yellow", "JJ"),("dog", "NN"),
            ("barked", "VBD"), ("at", "IN"),  ("the", "DT"), ("cat", "NN")]
resultado = cp_ingles.parse(oracion)
print(resultado)
resultado.draw()

# Español
gramatica_espanol = r"""
  NP: {<DT|PP\$>?<NN>*<JJ>} 
      {<NNP>+}                
"""
oracion2 = [("Luis", "NNP"), ("dejo", "VBD"), ("caer", "RP"),
           ("su", "PP$"),  ("pelota", "NN"), ("nueva", "JJ")]
cp_espanol = nltk.RegexpParser(gramatica_espanol)
resultado2 = cp_espanol.parse(oracion2)
print(resultado2)
resultado2.draw()