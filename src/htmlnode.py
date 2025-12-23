class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    
    def to_html(self):
        raise NotImplementedError
    

    def props_to_html(self):
        if self.props:
            props_to_html = []
            for key, value in self.props.items():
                props_to_html.append(f"{key}=\"{value}\"")

            return " ".join(props_to_html)
        return "''"

    
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

        