class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    
    def to_html(self):
        raise NotImplementedError
    

    def props_to_html(self):
        if self.props is None:
            return ""
        

        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
      

    
    def __eq__(self,other_node):
        if not isinstance(other_node, HTMLNode):
            return NotImplemented
        

        if self.tag == other_node.tag:
            if self.value== other_node.value:
                if self.children == other_node.children:
                    if self.props == other_node.props:
                        return True
        return False
    

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

        