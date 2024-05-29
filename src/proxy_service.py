import win32serviceutil
import win32service
import win32event
import subprocess
import os


class ProxyService(win32serviceutil.ServiceFramework):
    _svc_name_ = "ProxyService"
    _svc_display_name_ = "URL Filtering Proxy Service"
    _svc_description_ = "A service that filters URLs using a machine learning model."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        executable_path = os.path.join(os.path.dirname(__file__), "proxy.py")
        self.process = subprocess.Popen(["mitmdump", "-s", executable_path])
        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)
        self.process.terminate()


if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(ProxyService)
