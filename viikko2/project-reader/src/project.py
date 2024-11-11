class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"
    
    def _list_items(self, items):
        result_string = ""
        if len(items) > 0:
            for item in items:
                result_string += f"\n- {item}"
        else:
            result_string = "-"
        return result_string

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license}\n"
            f"\nAuthors:{self._list_items(self.authors)}\n"
            f"\nDependencies:{self._list_items(self.dependencies)}\n"
            f"\nDevelopment dependencies:{self._list_items(self.dev_dependencies)}"
        )
