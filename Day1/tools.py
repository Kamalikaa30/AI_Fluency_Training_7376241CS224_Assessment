"""Tools available to the Student Placement AI Agent."""

import ast
import operator

from config import STUDENTS


# ---------------------------------------------------------
# Tool 1: Get private student data
# ---------------------------------------------------------

def get_student_data(student_name: str) -> str:
    """Return private placement data for one student."""

    for name, data in STUDENTS.items():
        if name.lower() == student_name.strip().lower():
            return (
                f"Student: {name}; "
                f"Skill: {data['skill']}; "
                f"LeetCode: {data['leetcode']}; "
                f"Aptitude: {data['aptitude']}; "
                f"Eligible: {data['eligible']}"
            )

    return f"Unknown student: {student_name}"


# ---------------------------------------------------------
# Tool 2: Calculator
# ---------------------------------------------------------

_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
}


def _evaluate(node):
    if isinstance(node, ast.Constant) and isinstance(
        node.value, (int, float)
    ):
        return node.value

    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](
            _evaluate(node.left),
            _evaluate(node.right)
        )

    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](
            _evaluate(node.operand)
        )

    raise ValueError("Unsupported expression")


def calculator(expression: str) -> str:
    """Evaluate basic arithmetic such as (85 + 91) / 2."""

    try:
        result = _evaluate(
            ast.parse(expression, mode="eval").body
        )
        return str(result)

    except Exception as error:
        return f"Calculator error: {error}"


# ---------------------------------------------------------
# Tool mappings
# ---------------------------------------------------------

TOOL_FUNCTIONS = {
    "get_student_data": get_student_data,
    "calculator": calculator,
}


# ---------------------------------------------------------
# Tool schemas given to the LLM
# ---------------------------------------------------------

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_student_data",
            "description": (
                "Get private placement data for a student, "
                "including skill, LeetCode score, aptitude score, "
                "and placement eligibility."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "student_name": {
                        "type": "string",
                        "description": "Student's name"
                    }
                },
                "required": ["student_name"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": (
                "Perform arithmetic using numbers, +, -, *, / "
                "and parentheses."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "Arithmetic expression"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]


# ---------------------------------------------------------
# Direct tool testing
# ---------------------------------------------------------

if __name__ == "__main__":
    print(
        "get_student_data('Anu') ->",
        get_student_data("Anu")
    )

    print(
        "get_student_data('Charan') ->",
        get_student_data("Charan")
    )

    print(
        "calculator('(85 + 91) / 2') ->",
        calculator("(85 + 91) / 2")
    )