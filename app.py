from flask import Flask, request, jsonify
from ast_rule_engine import Node

app = Flask(__name__)

rules = {}  # Dictionary to store rules by ID

@app.route('/create_rule', methods=['POST'])
def create_rule():
    rule_string = request.json.get('rule_string')
    ast = parse_rule_string_to_ast(rule_string)  # Parse rule string to AST
    rule_id = len(rules) + 1
    rules[rule_id] = ast
    return jsonify({"rule_id": rule_id})

@app.route('/evaluate_rule/<int:rule_id>', methods=['POST'])
def evaluate_rule(rule_id):
    data = request.json.get('data')
    rule_ast = rules.get(rule_id)
    if not rule_ast:
        return jsonify({"error": "Rule not found"}), 404
    result = rule_ast.evaluate(data)
    return jsonify({"result": result})

@app.route('/update_rule/<int:rule_id>', methods=['PUT'])
def update_rule(rule_id):
    new_rule_string = request.json.get('rule_string')  # Get the new rule string
    if rule_id not in rules:  # Check if rule exists
        return jsonify({"error": "Rule not found"}), 404

    try:
        ast = parse_rule_string_to_ast(new_rule_string)  # Parse new rule into AST
        rules[rule_id] = ast  # Update the rule
        return jsonify({"message": "Rule updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Handle errors

# This function parses the rule string and creates an AST
def parse_rule_string_to_ast(rule_string):
    if 'AND' in rule_string:
        parts = rule_string.split('AND')
        left = Node('operand', value=parts[0].strip())
        right = Node('operand', value=parts[1].strip())
        return Node('operator', left=left, right=right, value='AND')
    elif 'OR' in rule_string:
        parts = rule_string.split('OR')
        left = Node('operand', value=parts[0].strip())
        right = Node('operand', value=parts[1].strip())
        return Node('operator', left=left, right=right, value='OR')
    return Node('operand', value=rule_string.strip())

if __name__ == '__main__':
    app.run(debug=True)


