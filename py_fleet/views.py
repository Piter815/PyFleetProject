
from core.views import EmployeeListView

class IndexView(EmployeeListView):
    template_name = 'index.html'
    title = 'Welcome to Pyfleet!'