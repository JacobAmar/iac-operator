from git import Repo, Head
import os,subprocess

def git_handler(repository,path,branch=None):
            # Perform the git clone operation if the directory doesn't exist
    if not os.path.isdir(path):
        subprocess.run(["git", "clone", repository, path])
    if branch != None:
    # Checkout to the specific version
       subprocess.run(["git", "checkout", branch], cwd=path)
       subprocess.run(["git", "pull"])
    else:
        subprocess.run(["git", "pull"])

#def git_handler(repository,path,branch=None):
      #   if os.path.exists(path) == False:
      #      print(f"cloning the repository: {repository}")
      #      Repo.clone_from(repository,to_path=path,branch=branch)
      #   else:
      #           repo = Repo(path)
      #           remote = repo.remote(name='origin')
      #           if branch == None:
      #               print(f"pulling changes for repo {repository}")
      #               pull = remote.pull()
      #               for change in pull:
      #                     print(f"pulled changes for {change.name}")
      #           else:
      #                 # checking out to the spesific branch address any changes on the branch name
      #                 print(f"pulling changes for repo {repository}")
      #                 for ref in remote.refs:
      #                       if branch in ref.name:
      #                             # meaning, if the branch name is in the remote
      #                             print(f"branch found, {ref.name}")
      #                             remote.fetch()
      #                             ref.checkout()