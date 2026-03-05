def status_str(self, prefix=''):
    return '\n'.join(prefix + str(message) for message in sorted(self.messages))