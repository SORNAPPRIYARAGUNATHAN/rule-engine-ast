from ast_rule_engine import Node

def test_simple_rule():
    # Test an AST where age > 30 AND department == 'Sales'
    ast = Node('operator', 
               left=Node('operand', value='age > 30'), 
               right=Node('operand', value="department == 'Sales'"), 
               value='AND')
    
    # Sample data for testing
    data = {"age": 35, "department": "Sales"}
    
    assert ast.evaluate(data) == True
    print("Test passed: Age > 30 AND Department == 'Sales'.")

if __name__ == "__main__":
    test_simple_rule()
