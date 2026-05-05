from dataclasses import dataclass, asdict
import copy

@dataclass
class Skill:
  name: str
  description: str
  when_to_use: str
  example_queries: list[str]
  tags: list[str]

  @property
  def summary(self) -> str:
    return f"""
Name: {self.name}

Description: {self.description}

When to use: {self.when_to_use}

Example user queries:
{chr(10).join(f"- {q}" for q in self.example_queries)}

Keywords: {", ".join(self.tags)}
"""
  
  def dump(self):
    data = copy.deepcopy(asdict(self))
    if isinstance(data.get('example_queries'), list):
      data['example_queries'] = "\n\n".join(data['example_queries'])
        
    if isinstance(data.get('tags'), list):
      data['tags'] = "\n\n".join(data['tags'])
        
    return data