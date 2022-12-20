import numpy as np

class CalcNum:
    def evalFunction(self, function: str, x: float):
        return eval(function)

    def log(self, x):
        return np.log(x)

    def bisertion(self, a, b, tolerance, nIteration, function):
        prevX = float("nan")
        for i in range(nIteration):
            # Calcula x (ponto no meio do intervalo [a, b])
            x = (a + b) / 2
            fx = self.evalFunction(function, x)
            signal = self.evalFunction(function, a) * fx

            # Calcula Erro relativo.
            error = abs((x - prevX) / max(x, 1))

            # X Anterior.
            prevX = x

            print("Iteração {i:3d}: a={a:+.5f}, ".format(i=i, a=a) +
              "b={b:+.5f}, error={err:+.5f}, ".format(b=b, err=error) +
              "x={x:+.5f}, f(x)={fx:+.5f}, ".format(x=x, fx=fx) +
              "sinal={s:+.5f}".format(s=signal))

            # Verifica e exibe se a raiz foi encontrada
            if(fx == 0 or error < tolerance):
                print("Raiz aproximada encontrada: {r:+5.5f}".format(r=x))
                break

            # Verifica se o sinal de f(a) * f(x) é menor que zero
            if(signal > 0):
                # O próximo intervalo será [x, b]
                a = x
            else:
                # O próximo intervalo será [a, x]
                b = x

    def falsePosition(self, a: float , b: float, tolerance: float, nInterations: int, function: str):
        prevX = float("nan")
        for i in range(nInterations):
            x = (a * self.evalFunction(function, b) - b * self.evalFunction(function, a)) / (self.evalFunction(function, b) - self.evalFunction(function, a))

            error=abs((x-prevX)/max(x, 1))
            prevX = x
            result = self.evalFunction(function, x)*self.evalFunction(function, a)
            fx = self.evalFunction(function, x)

            print("Iteração {i:3d}: a={a:+.5f}, ".format(i=i, a=a) +
                "b={b:+.5f}, error={err:+.5f}, ".format(b=b, err=error) +
                "x={x:+.5f}, f(x)={fx:+.5f}, ".format(x=x, fx=fx) +
                "f(x) x f(a)={r:+.5f}".format(r=result))

            if(fx == 0 or error < tolerance):
                print("Raiz aproximada encontrada: {r:+5.5f}".format(r=x))
                break
            
            if(result > 0):
                a = x
            else:
                b = x

            if(i == 19):
                print("Raiz aproximada encontrada: {r:+5.5f}".format(r=x))
                break

    def fixedPoint(self, a: float, b: float, tolerance: float , nInterations: int, function: str):
        prevX = float('Nan')
        x = (a+b)/2
        for k in range(nInterations):
            prevX = x
            x = self.evalFunction(function, x)
            error = abs((x - prevX)/max(x,1))
            print(f'k={k}, x = {x:.6f}')
            if error < tolerance or x == prevX:
                print(f'Raiz aproximada encontrada: {x:.6f}')
                break

    def newtonRaphson(self, a: float, b, tolerance: float, nInterations: int, functionA: str, functionB: str):
        prevX = float("Nan")
        x = a
        
        for k in range(0, nInterations):
            error = abs((x - prevX)/(max(x, 1)))
            print(f'Iteração: {k}, x: {x:.6f}, f(x): {self.evalFunction(functionA, x):.6f}, erro: {error:.6f}')
            if self.evalFunction(functionA, x) == 0 or error < tolerance:
                break
            prevX = x
            x = x - (self.evalFunction(functionA, x)/ self.evalFunction(functionB, x))

        print(f'A raiz aproximada é: {x:.6f}')


    def secant(self, a: float, b: float, tolerance: float, N: int, function: str):
        step = 1
        condition = True
        xa = a
        while condition:
            if self.evalFunction(function, a) == self.evalFunction(function, b):
                print('Erro de divisão por zero!')
                break
            
            xa = a - (b-a)*self.evalFunction(function, a)/( self.evalFunction(function, b) - self.evalFunction(function, a) ) 
            a = b
            b = xa
            step = step + 1
            
            if step > N:
                print('Não convergente!')
                break
            
            condition = abs(self.evalFunction(function, xa)) > tolerance
        
        print(f'Raiz aproximada encontrada: {xa:.6f}')