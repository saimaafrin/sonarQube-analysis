from collections import Counter
import re
def task_func(result):
    # Extract values associated with the 'url' key
    urls = [item['url'] for item in result]
    
    # Use regular expression to extract domain from the URL
    domain_pattern = re.compile(r'https?://([^/]+)')
    domains = [domain_pattern.match(url).group(1) for url in urls if domain_pattern.match(url)]
    
    # Count the occurrences of each domain
    domain_counts = Counter(domains)
    
    return dict(domain_counts)