import requests
import re

class Repository:
  #
  # Get Repository
  #
  def __init__(self, user: str,repository: str):
      self.user = user
      self.repository = repository
  
  def get_repository(self):
    url = "https://api.github.com/repos/{}/{}/git/trees/master?recursive=1".format(self.user, self.repository)
    response = requests.get(url)
    return response.json()

class TreePath:
  #
  # List Tree Path
  #
  def __init__(self, response: str):
    self.response = response

  def tree_path(self):
    tree_path = []
    for tree in self.response['tree']:
      if (tree['path'].startswith('html/cgi-bin/')):
        text_tree = tree['path']
        captive = re.search("^html/cgi-bin/captive/.*.cgi",text_tree)
        logs = re.search("^html/cgi-bin/logs.cgi/.*.dat",text_tree)
        if (not captive and not logs):
          path = text_tree[13:]
          tree_path.append(path)
    return tree_path

class URLValidator():
  #
  # Status Code
  #
  def __init__(self,ip:str,path:str):
    self.path = path
    self.ip = ip

  def response_status_code(self):
    url_validator = []
    final_list = []
    for tree_path in self.path:
      response = requests.get('{}{}'.format(self.ip,tree_path))
      url_validator.append({
            'URL': '{}{}'.format(self.ip, tree_path),
            'STATUS': '{}'.format(response.status_code)
      })
    url_validator.sort(key=lambda item: item['STATUS'])
    for item in url_validator:
      final_list.append('URL: {} - STATUS: {}'.format(item['URL'],item['STATUS']))
    return final_list

class CreateTextFile:
  #
  # Create a file
  #
  def __init__(self,file_name: str, response: list[str]):
    self.file_name = file_name
    self.response = response
  
  def create_file(self):
    file = open(self.file_name, 'w+')
    for i in self.response:
      file.write("%s\r\n" % (i))
    file.close()


if __name__ == '__main__':
  user = "ipfire"
  repo = "ipfire-2.x"
  ip = 'https://github.com/ipfire/ipfire-2.x/tree/master/html/cgi-bin/'
  repository = Repository(user,repo).get_repository()
  tree = TreePath(repository).tree_path()
  validator = URLValidator(ip,tree).response_status_code()
  file = CreateTextFile('url_status_code.txt',validator).create_file()


