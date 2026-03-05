import os

def _eval_file(prefix, file_path):
    if not file_path.startswith(prefix):
        return None
    
    file_type = os.path.splitext(file_path)[1].lower()
    
    if file_type == '.xml':
        return None
    
    component_id = os.path.basename(file_path).split('.')[0]
    
    if file_type == '.pdf':
        return {'component_id': component_id, 'file_path': file_path}
    
    return {'component_id': component_id, 'file_path': file_path, 'ftype': file_type}