import sys 
sys.path.insert(0, r'd:\Dialora-main\backend') 
import local_ai 
print('TEST NON-STREAMING') 
print(local_ai.generate_ai_response('Hello, this is a test call.', context=[])) 
print('TEST STREAMING') 
import itertools 
gen=local_ai.get_ai_response_streaming('Hello, this is a test call.', context[]) 
print([next(gen) for _ in range(5)]) 
