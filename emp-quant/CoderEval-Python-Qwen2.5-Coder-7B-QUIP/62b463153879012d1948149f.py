import os

def _eval_file(prefix, file_path):
    if not file_path.startswith(prefix):
        return None
    
    if file_path.endswith('.xml'):
        return None
    
    component_id = os.path.splitext(file_path)[0]
    ftype = os.path.splitext(file_path)[1][1:]
    
    if ftype == 'pdf':
        return {'component_id': component_id, 'file_path': file_path}
    
    return {'component_id': component_id, 'file_path': file_path, 'ftype': ftype}