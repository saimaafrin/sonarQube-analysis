def status_str(self, prefix=''):
    return '\n'.join(f"{prefix}{msg}" for msg in sorted(self.messages))