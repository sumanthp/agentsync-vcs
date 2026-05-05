import yaml
from .base import BaseAdapter
from ..models import AgentRule

class HermesAdapter(BaseAdapter):
    def translate(self, rule: AgentRule) -> dict:
        # Hermes uses .hermes/skills/ with YAML frontmatter
        
        frontmatter = {
            "name": rule.name,
            "description": rule.description or f"Instructions for {rule.name}"
        }
        
        fm_str = yaml.safe_dump(frontmatter, sort_keys=False)
        content = f"---\n{fm_str}---\n{rule.body}"
        
        # Sanitize rule name for path safety
        safe_name = "".join(c for c in rule.name if c.isalnum() or c in ("-", "_")).strip()
        file_path = f".hermes/skills/{safe_name}.md"
        return {file_path: content}
