import math

def calculator():
    print("🔹 Advanced Calculator 🔹")
    print("Type 'exit' to quit")
    print("Available functions: +, -, *, /, %, **, sqrt, sin, cos, tan, log, log10, factorial")
    print("Example: 2 + 3 * sqrt(16)")

    while True:
        expr = input("\nEnter expression: ")

        if expr.lower() in ["exit", "quit", "q"]:
            print("Exiting Calculator. Goodbye! 👋")
            break

        try:
            # Allow math functions
            result = eval(expr, {"__builtins__": None}, {
                "sqrt": math.sqrt,
                "sin": math.sin,
                "cos": math.cos,
                "tan": math.tan,
                "log": math.log,      # natural log
                "log10": math.log10,  # base-10 log
                "pi": math.pi,
                "e": math.e,
                "factorial": math.factorial,
                "pow": math.pow
            })
            print("Result:", result)

        except Exception as e:
            print("❌ Error:", e)


if __name__ == "__main__":
    calculator()
