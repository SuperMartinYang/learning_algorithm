import sys
class Redirect_stdout:
    def __init__(self, out_new):
        self.out_new = out_new
    def __enter__(self):
        self.out_old = sys.stdout
        sys.stdout = self.out_new
    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout = self.out_old
        return

print('A')
with open('out.log', 'w') as file_t, Redirect_stdout(file_t):
    print('B')
print('C')