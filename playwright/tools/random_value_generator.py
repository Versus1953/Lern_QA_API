import random  
import string  

#Generate a random name that matches the pattern '^[a-zA-Z0-9._-]+$' and has a length > 1
import random
import string


# Generate a random name that matches the pattern '^[a-zA-Z0-9._-]+$' and has a length > 1
class RandomNameGenerator:

    increment_groups = {
            'small': [4, 5, 8, 10, 16, 20, 25, 32, 50, 64],
            'medium': [100, 120, 125, 128, 150, 160, 200, 240, 250, 256, 320, 400, 480, 500, 512],
            'large': [600, 640, 750, 800, 960, 1000, 1024, 1200, 1280, 1500, 1536, 1600, 2000, 2048, 2500, 2560, 3000, 4000, 4096, 8000, 8192]
        }
    @staticmethod
    def generate_object_name(min_length=16, max_length=30):
        if min_length < 11:
            raise ValueError("Minimum length must be at least 11 characters.")
        # Define which characters are allowed:
        # - ASCII letters (both lowercase and uppercase)
        # - Digits (0-9)
        # - Special characters: period (.), underscore (_), and hyphen (-)
        allowed_chars = string.ascii_letters + string.digits + "._-"
        length = random.randint(min_length, max_length)
        return "".join(random.choices(allowed_chars, k=length))
    
    @staticmethod
    def generate_int(min_value=1, max_value=1000):
        """
        Generate a random integer within the specified range.
        """
        return random.randint(min_value, max_value)

    @staticmethod
    def generate_int_as_string(min_value=1, max_value=1000):
        """
        Generate a random integer as a string within the specified range.
        """
        return str(random.randint(min_value, max_value))
    
    
    @staticmethod
    def generate_hostname_name(parts_min=2, parts_max=4, include_numbers=True):
        """
        Generate a domain-like name with pattern similar to 'example.com'
        """
        def random_component(min_len=2, max_len=6, allow_numbers=True):
            chars = string.ascii_lowercase
            if allow_numbers and include_numbers and random.random() > 0.7:
                chars += string.digits
            length = random.randint(min_len, max_len)
            return "".join(random.choices(chars, k=length))
        
        def random_tld_component(min_len=2, max_len=3):
            # TLD -only letters
            chars = string.ascii_lowercase
            length = random.randint(min_len, max_len)
            return "".join(random.choices(chars, k=length))
        
        num_parts = random.randint(parts_min, parts_max)
        components = [random_component() for _ in range(num_parts)]
    
        tld = random_tld_component(2, 3)
        domain = f"{random_component(2, 3)}.{tld}"
        components.append(domain)
        
        return ".".join(components)
    
    @staticmethod
    def generate_resolver_name(parts_min=2, parts_max=4, include_numbers=True):
        def random_component(min_len=2, max_len=6, allow_numbers=True):
            chars = string.ascii_lowercase
            if allow_numbers and include_numbers and random.random() > 0.7:
                chars += string.digits
            length = random.randint(min_len, max_len)
            return "".join(random.choices(chars, k=length))
        
        def random_tld_component(min_len=2, max_len=3):
            # TLD - only letters
            chars = string.ascii_lowercase
            length = random.randint(min_len, max_len)
            return "".join(random.choices(chars, k=length))
        
        # Generate resolver prefix randomly
        prefix_parts = [
            random_component(2, 3, allow_numbers=False),
            random_component(2, 3, allow_numbers=False)
        ]
        prefix = "".join(prefix_parts)
        
        num_parts = random.randint(parts_min, parts_max)
        components = [random_component() for _ in range(num_parts)]
        
        tld = random_tld_component(2, 3)
        domain = f"{random_component(2, 3)}.{tld}"
        components.append(domain)
        
        components.insert(0, prefix)
        
        return ".".join(components)


    @staticmethod
    def generate_random_number_storage(group=None):
        increment_groups = {
            'small': ['20', '25', '32', '50', '64'],
            'medium': ['100', '120', '125', '128', '150', '160', '200', '240', '250', '256', '320', '400', '480', '500', '512'],
            'large': ['600', '640', '750', '800', '960', '1000', '1500', '2000']
        }
        
        if group is None:
            group = random.choice(list(increment_groups.keys()))
        if group not in increment_groups:
            raise ValueError(f"Invalid group: {group}. Must be one of: {list(increment_groups.keys())}")
        return random.choice(increment_groups[group])
    
    
    @staticmethod
    def generate_random_iops_limit(group=None):      
        iops_groups = {
            'small': ['500', '1000', '1500', '2000', '2500', '3000'],
            'medium': ['5000', '7500', '10000', '15000', '20000', '25000'],
            'large': ['30000', '40000', '50000', '60000', '70000', '80000', '90000', '100000'],
            
        }        
        if group is None:
            group = random.choice(list(iops_groups.keys()))
        if group not in iops_groups:
            raise ValueError(f"Invalid category: {group}. Must be one of: {list(iops_groups.keys())}")
        return random.choice(iops_groups[group])

    @staticmethod
    def generate_random_mbps_limit(group=None):       
        mbps_groups = {
            'small': ['50', '75', '100', '125', '150'],
            'medium': ['200', '250', '300', '350', '400'],
            'large': ['1000', '1500', '2000', '2500', '3000', '4000']
        }        
        if group is None:
            group = random.choice(list(mbps_groups.keys()))
        if group not in mbps_groups:
            raise ValueError(f"Invalid category: {group}. Must be one of: {list(mbps_groups.keys())}")
        return random.choice(mbps_groups[group])
    
    def generate_mbps_value(self, group: str = 'medium') -> str:
   
        mbps_ranges = {
            'minimal': (1, 50),      
            'small': (51, 200),     
            'medium': (201, 500),    
            'large': (501, 1000),    
            'xlarge': (1001, 2000)  
        }
        
        if group not in mbps_ranges:
            group = 'medium'
        
        min_val, max_val = mbps_ranges[group]
        return str(random.randint(min_val, max_val))
    
name_generator = RandomNameGenerator()


 

  
