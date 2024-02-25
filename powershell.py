from pypsrp.powershell import PowerShell, RunspacePool
from pypsrp.wsman import WSMan

import enum
import paramiko

class Perms(enum.Enum):
    Full = 0,
    ReadOnly = 1
    pass
    	
	
class powershell_connection(WSMan):
    def __init__(self, fs_fqdn: str, ps_user: str, ps_user_password: str):
        self.__fs_fqdn = fs_fqdn
        self.__ps_user = ps_user
        self.__ps_user_password = ps_user_password
        self.dirs = {}
        
        self.ps_conn = super().__init__(self.__fs_fqdn, username=self.__ps_user, password=self.__ps_user_password, ssl=False, auth='basic', encryption='never')
	
    def get_permissons(self, path_to_script_acl: str):
        with self.ps_conn, RunspacePool(self.ps_conn) as powershell:
    
	# execute PS script for getting ACL
            ps = PowerShell(powershell)
            ps_script = None

        with open(path_to_script_acl, 'r') as reader:
            ps_script = reader.read()
            reader.close()
            pass
        ps.add_script(ps_script)
        output = ps.invoke()
        for dir in ps.output:
            if self.dirs.get(str(dir.extended_properties['Folder Name'])) == None:
                self.dirs[str(dir.extended_properties['Folder Name'])] = []
                pass
            if str(dir.extended_properties['Group/User']) not in ['BUILTIN\\Administrators', 'FS01\\Administrator', 'NT AUTHORITY\\SYSTEM']: 
                self.dirs[str(dir.extended_properties['Folder Name'])].append({str(dir.extended_properties['Group/User']): str(dir.extended_properties['Permissions'])})
                pass
            pass
        print(self.dirs.items())
  