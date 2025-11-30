from strands import tool

@tool(name="calculator", description="Resolve expressões matemáticas")
def calculate_expression(expression: str):
    try:
        resultado = eval(expression)
        return resultado
    except:
        return "Erro no cálculo"