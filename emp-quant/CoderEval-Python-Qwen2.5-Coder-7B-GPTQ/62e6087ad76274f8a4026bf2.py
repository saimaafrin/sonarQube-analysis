self.output_queue.append({
    'type': 'DISCARD',
    'n': n,
    'qid': qid,
    'dehydration_hooks': dehydration_hooks,
    'hydration_hooks': hydration_hooks,
    'handlers': handlers
})