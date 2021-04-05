import pickle

class cookies:
  '''first
  >>> from PyCookie import cookies
  '''
  @staticmethod
  def save(cookie, file_name):
    '''Save your cookies
    >>> cookies.save(your_cookies, file_name)
    '''
    with open(file_name, 'wb') as file:
      pickle.dump(cookie, file)
      file.close()

  @staticmethod
  def load(file_name):
    '''load your cookies
    >>>cookies.load(file_name)
    '''
    with open(file_name, 'rb') as file:
      fi = pickle.load(file_name)
      file.close()
      return fi
