from functools import wraps

def arg_checker(*arg_types):
    '''An argument checker decorator that checks both:
        - The number of variables that you use for a function
        - The type of each variable.
       Raises a TypeError if either of these fail''' 
    def decorator(func):
        @wraps(func)  
        def wrapper(args):
            if len(arg_types)> len(args) or len(arg_types)<len(args):
                raise TypeError('Please fulfill the number of args requirements')
            elif len(arg_types)==len(args):
                for i in range(len(args)):
                    if Type(args[i])!=Type(arg_types[i]):
                        raise TypeError(f'Please pass the requested type for the argument {args[i]}')
                return func(*args)
            return wrapper
        return decorator   
                    
                    
                    
       
    
