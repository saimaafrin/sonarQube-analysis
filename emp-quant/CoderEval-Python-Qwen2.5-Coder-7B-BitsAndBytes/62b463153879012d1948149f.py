import os

def _eval_file(prefix, file_path):
    if not file_path.startswith(prefix):
        return None
    
    _, ext = os.path.splitext(file_path)
    
    if ext == '.xml':
        return None
    
    component_id = os.path.basename(file_path).split('.')[0]
    
    if ext == '.pdf':
        return {'component_id': component_id, 'file_path': file_path}
    
    return {'component_id': component_id, 'file_path': file_path, 'ftype': ext[1:]}