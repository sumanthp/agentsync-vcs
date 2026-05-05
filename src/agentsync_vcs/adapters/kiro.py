from .base import BaseAdapter
from ..models import AgentRule

class KiroAdapter(BaseAdapter):
    def translate(self, rule: AgentRule) -> dict:
        # Kiro uses plain markdown in .kiro/steering/
        
        content_lines = []
        if rule.description:
            content_lines.append(f"> {rule.description}\n")
        
        content_lines.append(rule.body)
        content = "\n".join(content_lines).strip() + "\n"
        
        # Sanitize rule name for path safety
        safe_name = "".join(c for c in rule.name if c.isalnum() or c in ("-", "_")).strip()
        file_path = f".kiro/steering/{safe_name}.md"
        return {file_path: content}
