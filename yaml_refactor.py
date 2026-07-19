import os
import yaml
import glob

project_files = glob.glob('_projects/*.md')
projects_data = []

for file in project_files:
    with open(file, 'r') as f:
        content = f.read()
    
    # parse yaml front matter
    if content.startswith('---\n'):
        end_idx = content.find('---\n', 4)
        if end_idx != -1:
            yaml_str = content[4:end_idx]
            data = yaml.safe_load(yaml_str)
            # Add to data list
            # We remove layout since it belongs to the stub
            del data['layout']
            projects_data.append(data)
            
            # Rewrite stub
            stub = f"---\nlayout: project\nslug: {data['slug']}\n---\n"
            with open(file, 'w') as f2:
                f2.write(stub)

# Sort projects by project-N thumbnail number just to keep some order
def get_num(p):
    # e.g., images/project-1/2.png -> 1
    import re
    match = re.search(r'project-(\d+)', p.get('thumbnail', ''))
    return int(match.group(1)) if match else 99

projects_data.sort(key=get_num)

with open('_data/projects.yml', 'w') as f:
    yaml.dump(projects_data, f, sort_keys=False, default_flow_style=False, allow_unicode=True)

print("Refactored to _data/projects.yml")
