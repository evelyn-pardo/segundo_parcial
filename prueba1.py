def mayuscula(oracion):
     nueva = oracion[0]
     for i, v in enumerate(oracion):
          if i != 0:
              if oracion[i - 1] == ' ':
                  nueva += v.upper()
              else:
                  nueva += v
     return nueva

