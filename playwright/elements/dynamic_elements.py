
from elements.base_element import BaseElement

class DynamicRowElement(BaseElement):
    """Specialized class for dynamic row locators with different strategies"""
    
    LOCATOR_STRATEGIES = {
        "row-id": '[data-e2e-sheet-row-id="{identifier}"]',
        "cell-value": '[data-e2e-sheet-cell-value="{identifier}"]'
    }
    
    def __init__(self, page, identifier: str, strategy: str, name: str = None):
        if strategy not in self.LOCATOR_STRATEGIES:
            raise ValueError(f"Invalid locator strategy: {strategy}. Supported: {list(self.LOCATOR_STRATEGIES.keys())}")
        
        self.identifier = identifier
        self.strategy = strategy
        
        locator_template = self.LOCATOR_STRATEGIES[strategy]
        locator_str = locator_template.format(identifier=identifier)
        
        super().__init__(page, locator_str, name)
    
    @classmethod
    def row_attribute(cls, page, attribute_value: str, strategy: str):
        return cls(page, attribute_value, strategy, f"Row Value '{attribute_value}'")
   
